#!/usr/bin/python

import sys

highCost = 0.0

for line in sys.stdin:

    cost = float(line.strip())
    if float(cost) > float(highCost):
       highCost = cost

# Escribe o coste máis alto, unha vez rematado o bucle
print(str(highCost))