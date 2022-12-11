#!/usr/bin/python

import sys

highPrice = 0.0

for line in sys.stdin:
    sale = float(line.strip())
    if sale > highPrice:
       highPrice = sale

# Escribe o prezo más alto unha vez rematado o bucle
print(highPrice)
