#!/usr/bin/env python

from binascii import unhexlify
from base64 import b64encode

string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

print("Received: ", string)
print("Should:   ", expected)
print("UnHexed:  ", unhexlify(string))
print("b64enc:   ", b64encode(unhexlify(string)))

print("Matches:  ", b64encode(unhexlify(string)) == expected)
