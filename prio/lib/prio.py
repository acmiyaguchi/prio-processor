# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_prio')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_prio')
    _prio = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_prio', [dirname(__file__)])
        except ImportError:
            import _prio
            return _prio
        try:
            _mod = imp.load_module('_prio', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _prio = swig_import_helper()
    del swig_import_helper
else:
    import _prio
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def PrioPRGSeed_new():
    return _prio.PrioPRGSeed_new()
PrioPRGSeed_new = _prio.PrioPRGSeed_new

def PrioPRGSeed_cleanup(seed):
    return _prio.PrioPRGSeed_cleanup(seed)
PrioPRGSeed_cleanup = _prio.PrioPRGSeed_cleanup
CURVE25519_KEY_LEN = _prio.CURVE25519_KEY_LEN
CURVE25519_KEY_LEN_HEX = _prio.CURVE25519_KEY_LEN_HEX
PRIO_SERVER_A = _prio.PRIO_SERVER_A
PRIO_SERVER_B = _prio.PRIO_SERVER_B

def Prio_init():
    return _prio.Prio_init()
Prio_init = _prio.Prio_init

def Prio_clear():
    return _prio.Prio_clear()
Prio_clear = _prio.Prio_clear

def PrioConfig_new(n_fields, server_a, server_b, batch_id):
    return _prio.PrioConfig_new(n_fields, server_a, server_b, batch_id)
PrioConfig_new = _prio.PrioConfig_new

def PrioConfig_clear(cfg):
    return _prio.PrioConfig_clear(cfg)
PrioConfig_clear = _prio.PrioConfig_clear

def PrioConfig_numDataFields(cfg):
    return _prio.PrioConfig_numDataFields(cfg)
PrioConfig_numDataFields = _prio.PrioConfig_numDataFields

def PrioConfig_newTest(n_fields):
    return _prio.PrioConfig_newTest(n_fields)
PrioConfig_newTest = _prio.PrioConfig_newTest

def Keypair_new(pvtkey, pubkey):
    return _prio.Keypair_new(pvtkey, pubkey)
Keypair_new = _prio.Keypair_new

def PublicKey_import(pk, data):
    return _prio.PublicKey_import(pk, data)
PublicKey_import = _prio.PublicKey_import

def PublicKey_import_hex(pk, hex_data):
    return _prio.PublicKey_import_hex(pk, hex_data)
PublicKey_import_hex = _prio.PublicKey_import_hex

def PublicKey_export(pk, data):
    return _prio.PublicKey_export(pk, data)
PublicKey_export = _prio.PublicKey_export

def PublicKey_export_hex(pk, data):
    return _prio.PublicKey_export_hex(pk, data)
PublicKey_export_hex = _prio.PublicKey_export_hex

def PublicKey_clear(pubkey):
    return _prio.PublicKey_clear(pubkey)
PublicKey_clear = _prio.PublicKey_clear

def PrivateKey_clear(pvtkey):
    return _prio.PrivateKey_clear(pvtkey)
PrivateKey_clear = _prio.PrivateKey_clear

def PrioClient_encode(cfg, data_in, for_server_a, aLen, for_server_b, bLen):
    return _prio.PrioClient_encode(cfg, data_in, for_server_a, aLen, for_server_b, bLen)
PrioClient_encode = _prio.PrioClient_encode

def PrioPRGSeed_randomize(seed):
    return _prio.PrioPRGSeed_randomize(seed)
PrioPRGSeed_randomize = _prio.PrioPRGSeed_randomize

def PrioServer_new(cfg, server_idx, server_priv, server_shared_secret):
    return _prio.PrioServer_new(cfg, server_idx, server_priv, server_shared_secret)
PrioServer_new = _prio.PrioServer_new

def PrioServer_clear(s):
    return _prio.PrioServer_clear(s)
PrioServer_clear = _prio.PrioServer_clear

def PrioVerifier_new(s):
    return _prio.PrioVerifier_new(s)
PrioVerifier_new = _prio.PrioVerifier_new

def PrioVerifier_clear(v):
    return _prio.PrioVerifier_clear(v)
PrioVerifier_clear = _prio.PrioVerifier_clear

def PrioVerifier_set_data(v, data, dataLen):
    return _prio.PrioVerifier_set_data(v, data, dataLen)
PrioVerifier_set_data = _prio.PrioVerifier_set_data

def PrioPacketVerify1_new():
    return _prio.PrioPacketVerify1_new()
PrioPacketVerify1_new = _prio.PrioPacketVerify1_new

def PrioPacketVerify1_clear(p1):
    return _prio.PrioPacketVerify1_clear(p1)
PrioPacketVerify1_clear = _prio.PrioPacketVerify1_clear

def PrioPacketVerify1_set_data(p1, v):
    return _prio.PrioPacketVerify1_set_data(p1, v)
PrioPacketVerify1_set_data = _prio.PrioPacketVerify1_set_data

def PrioPacketVerify1_write(p, pk):
    return _prio.PrioPacketVerify1_write(p, pk)
PrioPacketVerify1_write = _prio.PrioPacketVerify1_write

def PrioPacketVerify1_read(p, upk, cfg):
    return _prio.PrioPacketVerify1_read(p, upk, cfg)
PrioPacketVerify1_read = _prio.PrioPacketVerify1_read

def PrioPacketVerify2_new():
    return _prio.PrioPacketVerify2_new()
PrioPacketVerify2_new = _prio.PrioPacketVerify2_new

def PrioPacketVerify2_clear(p):
    return _prio.PrioPacketVerify2_clear(p)
PrioPacketVerify2_clear = _prio.PrioPacketVerify2_clear

def PrioPacketVerify2_set_data(p2, v, p1A, p1B):
    return _prio.PrioPacketVerify2_set_data(p2, v, p1A, p1B)
PrioPacketVerify2_set_data = _prio.PrioPacketVerify2_set_data

def PrioPacketVerify2_write(p, pk):
    return _prio.PrioPacketVerify2_write(p, pk)
PrioPacketVerify2_write = _prio.PrioPacketVerify2_write

def PrioPacketVerify2_read(p, upk, cfg):
    return _prio.PrioPacketVerify2_read(p, upk, cfg)
PrioPacketVerify2_read = _prio.PrioPacketVerify2_read

def PrioVerifier_isValid(v, pA, pB):
    return _prio.PrioVerifier_isValid(v, pA, pB)
PrioVerifier_isValid = _prio.PrioVerifier_isValid

def PrioServer_aggregate(s, v):
    return _prio.PrioServer_aggregate(s, v)
PrioServer_aggregate = _prio.PrioServer_aggregate

def PrioTotalShare_new():
    return _prio.PrioTotalShare_new()
PrioTotalShare_new = _prio.PrioTotalShare_new

def PrioTotalShare_clear(t):
    return _prio.PrioTotalShare_clear(t)
PrioTotalShare_clear = _prio.PrioTotalShare_clear

def PrioTotalShare_set_data(t, s):
    return _prio.PrioTotalShare_set_data(t, s)
PrioTotalShare_set_data = _prio.PrioTotalShare_set_data

def PrioTotalShare_write(t, pk):
    return _prio.PrioTotalShare_write(t, pk)
PrioTotalShare_write = _prio.PrioTotalShare_write

def PrioTotalShare_read(t, upk, cfg):
    return _prio.PrioTotalShare_read(t, upk, cfg)
PrioTotalShare_read = _prio.PrioTotalShare_read

def PrioTotalShare_final(cfg, output, tA, tB):
    return _prio.PrioTotalShare_final(cfg, output, tA, tB)
PrioTotalShare_final = _prio.PrioTotalShare_final
# This file is compatible with both classic and new-style classes.


