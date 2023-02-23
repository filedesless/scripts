from base64 import b64decode
from Crypto.PublicKey import RSA
from gzip import decompress

# https://id0-rsa.pub/problem/43/

s = '''H4sIAIq6o1cAAy2QS5OiMBSF9/yaIDrVLnrRQfJS000gAbILhCJAUMryMfrrB6tndRf3u+ecexR2
nuLQNxF3eiU7u0IvitWtitimIcLrGEamFGdKxNmUx64hqq+xHyi++jZbd3JSQx1p3/QQBAbLBWCz
nRDQGbzocuws/ug0VkNz8g8br/fxKO51b8Ei+GwzCOon7JuTevNTHbFhmcBg/woo3t704qCWhM0k
T80TurqHvir5rEv6TrpZmNDG7wP1fLNFsQ0p5m9uMsVmpNiDQ3feB4cMXA9ZGAtpWd7DVEl2zOSx
y4DSvzuwz6WLLBCikPOhDmdmiB7yEQkhWSwlSqrSwsUUBtnkYF4yYxJdfOPHJc2VaPF2rkox1IPj
lVep9VAJoJzuZtJOi8aKsQa7hEdfF0H4VO/4TxbZW6B2ycbsPMyIpy2+Si7/mpzwtUX6zndfoRmT
1/4FYROKix05q4mjQvE/sbdeK9cLUN3b0X3LhIWBJLBKw5kuL5CjfDyKUnkl5cYixESCRCrp/n8V
KB/TTiIV54nf0eSKit8arnH3+Rn8A9M9NCIXAgAA
'''

c = int('391502e0b40dee0bbd2f61d1b25cfad1a0e629f65d47dbb2a723aee27e249fb012afd8046c8e4da36f1c8f2b771985dfd139adbb3196b54cd1af8d691e0a16a14a4d3b7ebf1d5a2c560a3f11f65d4636ad2194f021dfeb1a6ed6e272806875f5', 16)

pubkey = "\n".join(map(bytes.decode, b64decode(
    decompress(b64decode(s))).splitlines()[4:]))

k = RSA.import_key(pubkey)
# factors from "Factorization of a 768-bit RSA modulus"
p = 33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489
q = 36746043666799590428244633799627952632279158164343087642676032283815739666511279233373417143396810270092798736308917

phi = (p-1)*(q-1)
d = pow(k.e, -1, phi)
print(pow(c, d, k.n))
