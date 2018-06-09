#!/usr/bin/env python3

from decrypt import *

lines = [line.strip() for line in open('4.txt')]

m = filter(lambda l: l != [],
        map(potential_solutions, lines))

print(list(m))
