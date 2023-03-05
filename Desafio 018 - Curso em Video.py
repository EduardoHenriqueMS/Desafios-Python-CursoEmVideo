# Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.

from math import (cos, sin, tan, degrees)

valor = float(input('\n Digite o valor em radianos do ângulo:'))

seno = sin(valor)
cosseno = cos(valor)
tangente = tan(valor)
graus = degrees(valor)


print('\n O ângulo de {} radianos que corresponde a {:.2f} graus tem: \n seno = {} \n cosseno = {} \n tangente = {}'.format(valor, graus, seno, cosseno, tangente))


