# Crie um programa que leia um número real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 te a parte inteira 6.

from math import (floor)

num1 = float(input('\n Digite um número:'))
inteira = floor(num1)

print('\n A parte inteira de {} é {}'.format(num1, inteira))

# -------------------------------------------------------------------------
# Outra forma de fazer

import math

valor = float(input('\n Digite um número:'))

inteiro = math.floor(valor)

print('\n A parte inteira de {} é {}'.format(valor, inteiro))






