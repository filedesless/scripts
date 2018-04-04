#!/usr/bin/env python3

import sys

# terribly unsecure rsa demystification for myself

# extended euclidian algo
def egcd(b, n):
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    #return (b, x0, y0)
    return abs(x0)

# euclidian algo
def gcd(u, v):
    return u if v is 0 else gcd(v, u % v)

# Choose two differents large
# prime numbers

if len(sys.argv) < 3:
    p, q = 4079, 4729
    #p, q = 997, 661
    #p, q = 661, 167
else: 
    p, q = int(sys.argv[1]), int(sys.argv[2])
print("p, q =>", p, q)

# Calculate n = pq
n = p * q
print("n =>", n)

# Calculate t(n) = (p-1)(q-1)
t = (p-1) * (q-1)
print("t =>", t)

# Choose 1 < e < t | gcd(e, t) = 1
for e in range(2, t):
    if gcd(e, t) == 1:
        break
print("e =>", e)

# Compute ex + dy = 1 (mod t)
d = egcd(e, t)
print("d =>", d)
