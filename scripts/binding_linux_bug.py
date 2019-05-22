#!/usr/bin/env python3

from prio.libprio import (
    PRIO_SERVER_A,
    PublicKey_import_hex,
    PrioConfig_new,
    PrioTotalShare_new,
    PrioTotalShare_read,
    PrioTotalShare_final,
)
import array
from base64 import b64decode

batch_id = b"test"
n_data = 3
server_id = PRIO_SERVER_A
shared_secret = b64decode("m/AqDal/ZSA9597GwMM+VA==")
private_key_hex = b"19DDC146FB8EE4A0B762A7DAE7E96033F87C9528DBBF8CA899CCD1DB8CD74984"
public_key_hex_internal = b"445C126981113E5684D517826E508F5731A1B35485BACCD63DAA8120DD11DA78"
public_key_hex_external = b"01D5D4F179ED233140CF97F79594F0190528268A99A6CDF57EF0E1569E673642"
data_internal = b64decode("AJOrGbGbxCWweMLThk6rMEYxTTtpZT5usxSqcpVnppIJmaoA2A==")
data_external = b64decode("AZOrZk5kO9pPhz00ebarT7nOssSWmsGZTO+rf41qmFlt9mZd/yo=")

public_key_internal = PublicKey_import_hex(public_key_hex_internal)
public_key_external = PublicKey_import_hex(public_key_hex_external)

config = PrioConfig_new(n_data, public_key_internal, public_key_external, batch_id)

share_internal = PrioTotalShare_new()
share_external = PrioTotalShare_new()

PrioTotalShare_read(share_internal, data_internal, config)
PrioTotalShare_read(share_external, data_external, config)

final = PrioTotalShare_final(config, share_internal, share_external)
final = list(array.array("L", final))
print(final)