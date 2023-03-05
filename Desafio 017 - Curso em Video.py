# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import (hypot)

oposto = float(input('Digite o tamanho do cateto oposto:'))
adjacente = float(input('Digite o tamanho do cateto adjacente:'))

hipo = hypot(oposto, adjacente)

print('O tamanho da hipotenusa é: {:.2f}'.format(hipo))

# --------------------------------------------------------------------------
# Outra forma de fazer

import math

op = float(input('Digite o comprimento do cateto oposto:'))
ad = float(input('Digite o comprimento do cateto adjacente:'))

hi = math.hypot(op, ad)

print('O comprimento da hipotenusa é: {:.2f}'.format(hi))


