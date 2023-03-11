# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.
# Ex.: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Escreva o nome completo da pessoa:')).strip()

lista = nome.split()

print('O primeiro nome é: {}'.format(lista[0]))
print('O último nome é: {}'.format(lista[len(lista)-1]))
