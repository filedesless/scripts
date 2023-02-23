from Crypto.PublicKey import RSA
from math import gcd

# https://id0-rsa.pub/problem/8/

# here's a public key
pub1 = RSA.import_key('''-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKzl5VggSXb/Jm2oqkPeRQwtpmGlLnJT
Nre4LKx3VUljtLzYWj4xoG+aHBouwJT7DyeibpasCH8Yderr4zIGTNUCAwEAAQ==
-----END PUBLIC KEY-----''')

# and another one, who happens to share a factor with it
pub2 = RSA.import_key('''-----BEGIN PUBLIC KEY-----
MF0wDQYJKoZIhvcNAQEBBQADTAAwSQJCAPsrpwx56OTlKtGAWn24bo5HUg3xYtnz
nTj1X/8Hq7pLYNIVE57Yxoyr3zTOOBJufgTNzdKS0Rc5Ti4zZUkCkQvpAgMBAAE=
-----END PUBLIC KEY-----''')

# message encrypted using the first key
c = 0xf5ed9da29d8d260f22657e091f34eb930bc42f26f1e023f863ba13bee39071d1ea988ca62b9ad59d4f234fa7d682e22ce3194bbe5b801df3bd976db06b944da

# find factors of first key
p = gcd(pub1.n, pub2.n)
q = pub1.n // p

# compute private exponent
phi = (p - 1) * (q - 1)
d = pow(pub1.e, -1, phi)

# decrypt message
m = pow(c, d, pub1.n)
print(hex(m)[2:])
