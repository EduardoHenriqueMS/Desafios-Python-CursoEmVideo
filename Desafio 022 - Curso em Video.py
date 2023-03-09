# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas as letras minúsculas.
# - Quantas letras no total (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite o nome da pessoa:')).strip()

print('O nome com todas as letras maiúsculas é: {}'.format(nome.upper()))


print('O nome com todas as letras minúsculas é: {}'.format(nome.lower()))


print('O nome {} tem {} letras'.format(nome, len(nome) - nome.count(' ')))

variavel = nome.split()
print('O primeiro nome tem {} letras'.format(len(variavel[0])))



