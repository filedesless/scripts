#!/usr/bin/env python3

from binascii import unhexlify
from string import ascii_letters, digits

challenge = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def potential_solutions(string):
    printable = ascii_letters + digits + ' .,?"\' \n\t'
    b = unhexlify(string)

    f = filter(lambda s: all([c in bytes(printable, 'utf-8') for c in s]), 
            map(lambda x: bytes([c ^ x for c in b]), range(256)))

    return list(f)

if __name__ == "__main__":
    print(potential_solutions(challenge))
