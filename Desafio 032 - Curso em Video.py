# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano: '))

print('---' * 20)

if ano % 4 == 0:
    print('O ano {} é um ano BISSEXTO.'.format(ano))

else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))