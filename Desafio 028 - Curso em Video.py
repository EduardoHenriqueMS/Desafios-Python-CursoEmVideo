# Escreva um programa que faça o computador "pensar" em um número inteiro entre
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
# computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import (randint)
from time import (sleep)

valor = randint(0, 5)

escolhido = int(input('Escrevendo um número de 0 a 5 e tente adivinhar qual o computador escolheu:'))
print('---' * 40)
print('PROCESSANDO . . .')
print('---' * 40)
sleep(2)

numero = print('O computador escolheu o número {}'.format(valor))

if escolhido == valor:
    print('VOCÊ VENCEU!')

elif escolhido > 5:
    print('ERRO! Escolha um número inteiro entre 0 e 5.')

elif escolhido < 0:
    print('ERRO! Escolha um número inteiro entre 0 e 5.')

else:
    print('VOCÊ PERDEU!')

