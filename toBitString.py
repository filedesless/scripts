#!/usr/bin/env python3

# simple recursive function the shows the binary representation of an int

def toBitString(n: int) -> str: 
    return ("" if n < 2 else toBitString(n // 2)) + str(n % 2)

print(toBitString(4))
print(toBitString(6))
print(toBitString(1))
print(toBitString(11))
