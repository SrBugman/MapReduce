#!/usr/bin/python

import sys

totalCost = 0.0

for line in sys.stdin:

    totalCost += float(line.strip())

# Escribe o coste mais alto, unha vez rematado o bucle
print('O total de vendas foi de ' + str(totalCost))