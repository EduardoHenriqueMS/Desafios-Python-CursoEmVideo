# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import (choice)

alun1 = str(input('Escreva o nome do primeiro aluno:'))
alun2 = str(input('Escreva o nome do segundo aluno:'))
alun3 = str(input('Escreva o nome do terceiro aluno:'))
alun4 = str(input('Escreva o nome do quarto aluno:'))

lista = [alun1, alun2, alun3, alun4]

esc = choice(lista)

print('O aluno escolhido foi: {}'.format(esc))
