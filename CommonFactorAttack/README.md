# Common Factor Attack

from: http://www.loyalty.org/~schoen/rsa/

Sample C program that generates an RSA private key from discovered values of p and q.

### How to build

```
mkdir build
cd build
cmake ..
make
```

### examples for the scripts

```
./genkeys.py 911 919
p, q => 911 919
n => 837209
t => 835380
e => 11
d => 227831
./crypt.py 837209 11 hello
472264:657337:52461:52461:703046
./decrypt.py 837209 227831 472264:657337:52461:52461:703046
hello
```