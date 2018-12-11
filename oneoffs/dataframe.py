from prio.libprio import *
import pandas as pd 
import sys
from collections import namedtuple

# data -> verify1
def process_verify1(series, init_cb):
    s = init_cb()
    print(s)
    verifier = PrioVerifier_new(s.server)
    verify1 = PrioPacketVerify1_new()
    items = []
    for item in series:
        PrioVerifier_set_data(verifier, item)
        PrioPacketVerify1_set_data(verify1, verifier)
        data = PrioPacketVerify1_write(verify1)
        items.append(data)
    return pd.Series(items)

# verify1_a, verify1_b -> verify2
def process_verify2(df, init_cb):
    s = init_cb()
    print(s)
    verifier = PrioVerifier_new(s.server)
    v1A = PrioPacketVerify1_new()
    v1B = PrioPacketVerify1_new()
    v2 = PrioPacketVerify2_new()
    items = []
    for row in df.itertuples():
        PrioPacketVerify1_read(v1A, row.verify1_a, s.config)
        PrioPacketVerify1_read(v1B, row.verify1_b, s.config)
        PrioPacketVerify2_set_data(v2, verifier, v1A, v1B)
        data = PrioPacketVerify2_write(v2)
        items.append(data)
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


n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
k = int(sys.argv[2]) if len(sys.argv) > 2 else 100
pd.set_option('display.max_colwidth', -1)

print(f"{n} rows, {k} modulus")

skA, pkA = Keypair_new()
skB, pkB = Keypair_new()
server_secret = PrioPRGSeed_randomize()
config = PrioConfig_new(k, pkA, pkB, b"test")

# reference counting
Server = namedtuple('Server', ['server', 'config', 'server_id'])
def init_server(server_id):
    sk = skA if server_id == PRIO_SERVER_A else skB
    server = PrioServer_new(config, server_id, sk, server_secret)
    return Server(server, config, server_id)

init_a_cb = lambda: init_server(PRIO_SERVER_A)
init_b_cb = lambda: init_server(PRIO_SERVER_B)

for_server_a, for_server_b = PrioClient_encode(config, bytes([1]*k))
df = pd.DataFrame([(for_server_a, for_server_b)]*n, columns=["data_a", "data_b"])
print(df.head().to_string())

v1A = process_verify1(df.data_a, init_a_cb)
v1B = process_verify1(df.data_b, init_b_cb)
verify1_df = pd.concat([v1A, v1B], axis=1, keys=["verify1_a", "verify1_b"])
print(verify1_df.head().to_string())

v2A = process_verify2(verify1_df, init_a_cb)
v2B = process_verify2(verify1_df, init_b_cb)
verify2_df = pd.concat([v2A, v2B], axis=1, keys=["verify2_a", "verify2_b"])
print(verify2_df.head().to_string())

x = validate_aggregate(verify2_df, init_a_cb)
y = validate_aggregate(verify2_df, init_b_cb)