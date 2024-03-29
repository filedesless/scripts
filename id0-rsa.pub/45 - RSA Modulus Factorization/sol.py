import string
from math import isqrt

# https://id0-rsa.pub/problem/45/


def read(s: str) -> int:
    return int(''.join([c for c in s if c in string.hexdigits]), 16)


modulus = '''
    00:cc:02:62:c3:76:4f:6d:1b:fa:48:5a:88:c0:56:
    6a:6d:68:cb:89:ac:38:2f:bb:c5:77:a4:86:2b:db:
    ce:11:1b:b5:99:60:ea:78:7f:13:2e:3f:dd:b9:c9:
    14:d0:d1:1d:15:6d:d4:33:a2:ad:ab:90:84:d4:8c:
    f5:8f:58:b4:28:04:80:59:66:ec:d3:18:ad:19:21:
    87:91:e1:4e:19:a8:d0:cf:34:41:e2:19:e5:e1:39:
    5e:b5:db:a1:fb:a1:1d:94:32:1a:34:eb:53:6c:51:
    f4:c4:4c:59:87:e7:4a:46:7b:5f:e2:ea:e8:d2:72:
    5d:63:f2:4f:ee:bf:d9:ca:74:6d:e9:3b:6f:d7:4e:
    d8:2f:ed:7d:bf:c3:a8:4b:0a:42:5f:52:50:3a:b7:
    19:08:a1:3a:c1:1a:9d:52:21:10:42:29:0a:e2:88:
    66:26:f6:79:35:dc:78:b7:d8:6b:a7:6d:3c:5e:08:
    5a:00:3d:ff:06:f9:14:18:7a:cc:36:8f:90:46:13:
    cb:d3:d5:2f:36:c8:b0:53:5f:9d:fe:ec:27:37:74:
    4a:d8:be:51:f6:6e:1d:47:02:61:a7:fd:7c:6d:a2:
    77:db:d2:f2:13:b4:4d:9e:82:42:a8:a5:b1:21:ac:
    c8:71:0b:ae:d3:d2:44:00:4e:4c:a5:60:d5:8e:75:
    6b:a7'''
privateExp = '''
    00:87:80:3a:2b:0b:44:db:fa:8e:35:4a:74:b4:13:
    71:a2:f3:cc:e4:c7:4f:96:5c:c8:5e:9c:17:45:c0:
    3b:d1:5f:2f:32:0d:8e:0e:b4:90:7f:d2:89:a9:a1:
    66:42:ff:f1:aa:4f:05:77:ba:60:51:a8:ae:a1:22:
    72:e3:60:0e:60:da:04:89:dc:f4:05:8d:c9:42:fc:
    e3:37:c0:87:08:41:f9:56:f6:a5:9f:d0:85:c0:1f:
    43:c9:d4:74:75:56:60:f8:12:83:17:8d:0a:1e:d3:
    1c:98:d9:01:4a:64:14:10:56:57:ac:b7:4c:26:a3:
    31:66:76:06:23:54:a8:0a:70:33:5a:67:06:75:f4:
    39:de:c0:88:03:de:f4:89:2c:4d:99:e2:0f:be:19:
    75:d7:67:36:79:ac:6f:16:83:53:07:ce:59:97:1c:
    86:5d:71:ed:ee:a9:ed:1a:93:c7:0a:37:e2:83:f2:
    70:de:a8:49:92:71:26:8d:86:f7:fc:4a:1b:4f:64:
    04:18:33:c6:2a:05:7d:fb:0b:48:f1:c4:f6:d3:51:
    67:32:38:a3:de:3b:45:06:eb:24:72:aa:f9:0b:91:
    4e:79:1c:3a:72:34:64:d9:16:9d:5e:ab:8e:0a:3f:
    8a:42:de:db:06:58:29:e8:b5:33:a8:9d:d3:ba:0a:
    00:a1'''
n = read(modulus)
d = read(privateExp)
e = 65537

# since de = 1 [phi]
# \exists i < e : de - 1 = i * phi
# phi = next(x//i for i in reversed(range(2*e)) if (x := (d*e-1)) % i == 0)
for i in reversed(range(1, e)):
    if (x := (d*e-1)) % i == 0:
        print("i", i, x, x // i)
        phi = x // i
        assert (d*e) % phi == 1
        # since    pq = n and
        #         phi = (p-1)(q-1)
        #             = pq - p - q + 1
        #   ==> p + q = pq - phi + 1
        #             = n - phi + 1
        # we can construct a second degree polynomial with roots p and q
        B, C = -(n - phi + 1), n
        D = pow(B, 2) - 4*C
        R = isqrt(D)
        if R**2 != D:  # ensure D is a perfect square
            continue
        assert R**2 == D
        p, q = (-B + R)//2, (-B - R)//2
        print("factors", p, q)
        assert q**2 + B*q + C == 0
        assert p*q == n
        s = min(p, q) % 100000007
        print("sol", s)
        break
