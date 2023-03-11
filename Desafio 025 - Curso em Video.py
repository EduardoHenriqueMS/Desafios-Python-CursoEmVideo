# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.

nome = str(input('Escreva o nome da pessoa:')).upper()

variavel = 'SILVA' in nome

print('A pessoa de nome {} tem SILVA no nome? {}'.format(nome, variavel))