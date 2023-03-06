# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alu1 = str(input('Digite o nome do aluno 1:'))
alu2 = str(input('Digite o nome do aluno 2:'))
alu3 = str(input('Digite o nome do aluno 3:'))
alu4 = str(input('Digite o nome do aluno 4:'))

geral = [alu1, alu2, alu3, alu4]

random.shuffle(geral)

print('A ordem de apresentação será: {}'.format(geral))

