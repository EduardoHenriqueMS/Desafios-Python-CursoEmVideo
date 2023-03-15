# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.

x = float(input('Digite o primeiro comprimento da reta: '))
y = float(input('Digite o segundo comprimento de reta: '))
z = float(input('Digite o terceiro comprimento de reta: '))

if x < y + z and y < x + z and z < x + y:
    print('Os comprimentos da retas de valores {}, {} e {} podem formar um triângulo.'.format(x, y, z))

else:
    print('Os comprimentos de retas de valores {}, {} e {} NÃO PODEM formar um triangulo.'.format(x, y, z))


