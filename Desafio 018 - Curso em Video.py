# Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.

from math import (cos, sin, tan, degrees)

valor = float(input('\n Digite o valor em radianos do ângulo:'))

seno = sin(valor)
cosseno = cos(valor)
tangente = tan(valor)
graus = degrees(valor)


print('\n O ângulo de {} radianos que corresponde a {:.2f} graus tem: \n seno = {} \n cosseno = {} \n tangente = {}'.format(valor, graus, seno, cosseno, tangente))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Outra forma de fazer

from math import (sin, cos, tan, radians)

valor1 = float(input('\n Digite o valor do ângulo em graus:'))

seno1 = sin(radians(valor1))
cosseno1 = cos(radians(valor1))
tangente1 = tan(radians(valor1))

print('\n O ângulo de {} tem seno igual {}'.format(valor1, seno1))
print('\n O ângulo de {} tem cosseno igual a {}'.format(valor1, cosseno1))
print('\n O ângulo de {} tem tangente igual a {}'.format(valor1, tangente1))
