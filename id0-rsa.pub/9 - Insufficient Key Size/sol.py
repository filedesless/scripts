# https://id0-rsa.pub/problem/9/

# import libnum
from sympy.ntheory import factorint
from Crypto.PublicKey import RSA

s = '''-----BEGIN RSA PUBLIC KEY-----
MA8CCA3150PxP2ofAgMBAAE=
-----END RSA PUBLIC KEY-----'''
# s = '''-----BEGIN RSA PUBLIC KEY-----
# MBYCD3AY9xf8ZmUVDBSIVPZMSQIDAQAB
# -----END RSA PUBLIC KEY-----'''

k = RSA.import_key(s)

# print(libnum.factorize(k.n))
print(factorint(k.n))
