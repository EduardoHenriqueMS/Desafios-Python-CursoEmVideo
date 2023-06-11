# Refaça o 'DESAFIO 035' dos triângulos acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais.
# Isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes.

# DESAFIO 035 - PERGUNTA
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.

c1 = float(input('Digite o primeiro comprimento de reta: '))
c2 = float(input('Digite o segundo comprimento de reta: '))
c3 = float(input('Digite o terceiro comprimento de reta: '))

print('---' * 20)

if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('As retas PODEM formar um triângulo!')
    if c1 == c2 == c3:
        print('O triângulo é EQUILÁTERO!')
    elif c1 == c2 != c3 or c1 != c2 == c3 or c1 == c3 != c2:
        print('O triângulo é ISÓSCELES!')
    elif c1 != c2 != c3:
        print('O triângulo é ESCALENO!')
    else:
        print('ERRO!')
else:
    print('As retas NÃO PODEM formar um triângulo!')
