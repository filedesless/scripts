# https://id0-rsa.pub/problem/9/

from sympy.ntheory import factorint
from Crypto.PublicKey import RSA

# smaller test key
# s = '''-----BEGIN RSA PUBLIC KEY-----
# MA8CCA3150PxP2ofAgMBAAE=
# -----END RSA PUBLIC KEY-----'''
s = '''-----BEGIN RSA PUBLIC KEY-----
MBYCD3AY9xf8ZmUVDBSIVPZMSQIDAQAB
-----END RSA PUBLIC KEY-----'''

k = RSA.import_key(s)

p, q = factorint(k.n).keys()
phi = (p-1)*(q-1)
d = pow(k.e, -1, phi)
print(str(hex(d))[2:])
