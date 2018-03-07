#!/usr/bin/env python3

import sys

def decrypt(n: int, d: int, c: int) -> int:
    return (c ** d) % n

if len(sys.argv) < 4:
    print("usage: ./crypt.py n d cipher")
    sys.exit(1)

n = int(sys.argv[1])
d = int(sys.argv[2])
cipher = sys.argv[3]

m = "".join(list(map(lambda x: chr(decrypt(n, d, int(x))), cipher.split(':'))))
print(m)
