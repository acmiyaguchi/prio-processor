#!/usr/bin/env python
# coding: utf-8

# # Prio size estimates

from prio.libprio import *
from array import array
from collections import OrderedDict
import pandas as pd

def calculate_sizes(k):
    pvtkey, pubkey = Keypair_new()
    cfg = PrioConfig_new(k, pubkey, pubkey, b"test")
    server_secret = PrioPRGSeed_randomize()

    sA = PrioServer_new(cfg, PRIO_SERVER_A, pvtkey, server_secret)
    sB = PrioServer_new(cfg, PRIO_SERVER_B, pvtkey, server_secret)

    for_server_a, for_server_b = PrioClient_encode(cfg, bytes([1]*k))

    # Setup verification
    vA = PrioVerifier_new(sA)
    vB = PrioVerifier_new(sB)
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

    # Check validity of the request
    PrioVerifier_isValid (vA, p2A, p2B)
    PrioVerifier_isValid (vB, p2A, p2B)

    PrioServer_aggregate(sA, vA)
    PrioServer_aggregate(sB, vB)

    # Collect from many clients and share data
    tA = PrioTotalShare_new()
    tB = PrioTotalShare_new()
    PrioTotalShare_set_data(tA, sA)
    PrioTotalShare_set_data(tB, sB)

    packet1_a = PrioPacketVerify1_write(p1A)
    packet1_b = PrioPacketVerify1_write(p1B)
    packet2_a = PrioPacketVerify2_write(p2A)
    packet2_b = PrioPacketVerify2_write(p2B)
    total_shares_a = PrioTotalShare_write(tA)
    total_shares_b = PrioTotalShare_write(tB)

    sizes = OrderedDict([
        ("bits", k),
        ("data_A", len(for_server_a)),
        ("data_B", len(for_server_b)),
        ("verify1_A", len(packet1_a)),
        ("verify1_B", len(packet1_b)),
        ("verify2_A", len(packet2_a)),
        ("verify2_B", len(packet2_b)),
        ("agg_share_A", len(total_shares_a)),
        ("agg_share_B", len(total_shares_b)),
    ])
    return sizes

results = []
for k in range(0, 2001, 100):
    sizes = calculate_sizes(k)
    results.append(sizes)

df = pd.DataFrame(results)
print(df.to_string())