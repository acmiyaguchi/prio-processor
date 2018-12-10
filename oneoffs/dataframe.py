from prio.libprio import *
import pandas as pd 

# schemas
# data_a
# data_b
# verify1_a
# verify1_b
# verify2_a
# verify2_b
# totalshare_a
# totalshare_b

# 2x public key, 1x private key, batch id, size, server_id, shared secret

# data -> verify1
def process_verify1(df, init_cb):
    s = init_cb()
    suffix = "a" if s.server_id == PRIO_SERVER_A else "b"
    verifier = PrioVerifier_new(s.server)
    verify1 = PrioPacketVerify1_new()
    def func(row):
        PrioVerifier_set_data(verifier, row[f'data_{suffix}'])
        PrioPacketVerify1_set_data(verify1, verifier)    
        return PrioPacketVerify1_write(verify1)
    return df.apply(func, axis=1)


# verify1_a, verify1_b -> verify2
def process_verify2(df, init_cb):
    s = init_cb()
    verifier = PrioVerifier_new(s.server)
    verify1_a = PrioPacketVerify1_new()
    verify1_b = PrioPacketVerify1_new()
    verify2 = PrioPacketVerify2_new()
    items = []
    for row in df.itertuples():
        PrioPacketVerify1_read(verify1_a, row.verify1_a, s.config)
        PrioPacketVerify1_read(verify1_b, row.verify1_b, s.config)
        PrioPacketVerify2_set_data(verify2, verifier, verify1_a, verify1_b)
        items.append(PrioPacketVerify2_write(verify2))
    return pd.Series(items)

# verify2_a, verify2_b -> totalshare_a
def validate_aggregate(df, init_cb):
    s = init_cb()
    verifier = PrioVerifier_new(s.server)
    verify2_a = PrioPacketVerify2_new()
    verify2_b = PrioPacketVerify2_new()
    for row in df.itertuples():
        PrioPacketVerify2_read(verify2_a, row.verify2_a, s.config)
        PrioPacketVerify2_read(verify2_b, row.verify2_b, s.config)
        PrioVerifier_isValid(verifier, verify2_a, verify2_b); print("ok")
        PrioServer_aggregate(s.server, verifier)
    tshare = PrioTotalShare_new()
    PrioTotalShare_set_data(tshare, s.server)
    return PrioTotalShare_write(tshare)


from functools import partial
import sys
from collections import namedtuple

# reference counting
Server = namedtuple('Server', ['server', 'config', 'server_id'])

n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
k = int(sys.argv[2]) if len(sys.argv) > 2 else 100

print(f"{n} rows, {k} modulus")

skA, pkA = Keypair_new()
skB, pkB = Keypair_new()
server_secret = PrioPRGSeed_randomize()

def init_server(server_id):
    config = PrioConfig_new(k, pkA, pkB, b"test")
    sk = skA if server_id == PRIO_SERVER_A else skB
    server = PrioServer_new(config, server_id, sk, server_secret)
    return Server(server, config, server_id)

init_a_cb = partial(init_server, PRIO_SERVER_A)
init_b_cb = partial(init_server, PRIO_SERVER_B)

# pointers to configs must be reference counted with the server.
sA = init_a_cb()
sB = init_b_cb()
for_server_a, for_server_b = PrioClient_encode(sA.config, bytes([1]*k))


# # Setup verification
vA = PrioVerifier_new(sA.server)
vB = PrioVerifier_new(sB.server)
PrioVerifier_set_data(vA, for_server_a)
PrioVerifier_set_data(vB, for_server_b)

# Produce a packet1 and send to the other party
p1A = PrioPacketVerify1_new()
p1B = PrioPacketVerify1_new()
PrioPacketVerify1_set_data(p1A, vA)
PrioPacketVerify1_set_data(p1B, vB)

# Produce packet2 and send to the other party
p2A = PrioPacketVerify2_new()
p2B = PrioPacketVerify2_new()
PrioPacketVerify2_set_data(p2A, vA, p1A, p1B)
PrioPacketVerify2_set_data(p2B, vB, p1A, p1B)

print(PrioPacketVerify2_write(p2A))
print(PrioPacketVerify2_write(p2B))

# Check validity of the request
PrioVerifier_isValid(vA, p2A, p2B)
PrioVerifier_isValid(vB, p2A, p2B)


df = pd.DataFrame([(for_server_a, for_server_b)]*n, columns=["data_a", "data_b"])

print(df.head().to_string())

v1A = process_verify1(df, init_a_cb)
v1B = process_verify1(df, init_b_cb)

verify1_df = pd.concat([v1A, v1B], axis=1)
verify1_df.columns = ["verify1_a", "verify1_b"]
print(verify1_df.head().to_string())

v2A = process_verify2(verify1_df, init_a_cb)
v2B = process_verify2(verify1_df, init_b_cb)

verify2_df = pd.concat([v2A, v2B], axis=1)
verify2_df.columns = ["verify2_a", "verify2_b"]
print(verify2_df.head().to_string())

x = validate_aggregate(verify2_df, init_a_cb)
y = validate_aggregate(verify2_df, init_b_cb)
