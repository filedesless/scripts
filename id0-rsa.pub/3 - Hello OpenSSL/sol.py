from Crypto.PublicKey import RSA

s = '''-----BEGIN RSA PRIVATE KEY-----
MIGtAgEAAiEA5tygpSZdOZUMfuO3oTGWR4cALBtWui5UzrQw2/8JlZ0CAwEAAQIh
AI9n4Yp1KFfKlHaF8d15tgUONQXn+e3aI+beFKoi2XipAhEA/ZkHPmcDwXIqloGr
minb1wIRAOkMdv7emMGd08gwwOQ6i6sCEQC0pjcXx9BQFCCsWDDCwAC/AhEAxYcn
JQeO+izH4JpSJB/rWQIRAOO9m6JHEWgzLYD+fe003vw=
-----END RSA PRIVATE KEY-----'''

c = 0x6794893f3c47247262e95fbed846e1a623fc67b1dd96e13c7f9fc3b880642e42

k = RSA.import_key(s)
m = pow(c, k.d, k.n)
print(str(hex(m))[2:])
