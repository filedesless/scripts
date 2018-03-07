#!/usr/bin/env python3

# terribly unsecure rsa demystification for myself

def gcd(u, v):
    return u if v is 0 else gcd(v, u % v)

# Choose two differents large
# prime numbers

p, q = 4079, 4729
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

# Compute d to satisfy de = 1 + kt
for d in range(n):
    if (d * e) % t == 1:
        break
print("d =>", d)
