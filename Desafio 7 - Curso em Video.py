# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média

nota1 = float(input('Escreva a nota que você tirou na primeira prova:'))
nota2 = float(input('Escreva a nota que você tirou na segunda prova:'))

media = (nota1 + nota2) / 2

print('A nota da sua primeira prova foi: {}'.format(nota1))
print('A nota da sua segunda prova foi: {}'.format(nota2))

print('A média entre as suas duas provas é: {}'.format(media))
