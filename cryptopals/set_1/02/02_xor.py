#!/usr/bin/env python3

from binascii import unhexlify, hexlify

s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"

expected = "746865206b696420646f6e277420706c6179"
res = ""

print("Received: ", s1, s2)

u1, u2 = unhexlify(s1), unhexlify(s2)
print("UnHexed: ", u1, len(u1), u2, len(u2))

res = bytes([a ^ b for a, b in zip(u1, u2)])

print("xor'd: ", res)

res = hexlify(res)
print("re-hexlified: ", res)

print(res.decode(), expected)
print("Matches: ", res.decode() == expected)
