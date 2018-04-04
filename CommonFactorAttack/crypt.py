#!/usr/bin/env python3

import sys

# efficient modular exponentiation algo
def pow(b: int, e: int, m: int) -> int:
    res = 1
    b = b % m
    while e > 0:
        if e & 1 == 1:
            res = (res * b) % m
        e >>= 1
        b = (b * b) % m
    return res

def crypt(n: int, e: int, m: int) -> int:
    return pow(m, e, n)

if len(sys.argv) < 4:
    print("usage: ./crypt.py n e mesage")
    sys.exit(1)

n = int(sys.argv[1])
e = int(sys.argv[2])
msg = sys.argv[3]

c = ":".join(list(map(lambda x: str(crypt(n, e, ord(x))), list(msg))))
print(c)
