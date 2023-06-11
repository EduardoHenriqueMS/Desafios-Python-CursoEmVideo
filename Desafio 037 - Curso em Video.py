# Escreva um programa que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a 'base de conversão':
# 1 para binário.
# 2 para octal.
# 3 para hexadecimal.

numero = int(input('Digite um número inteiro qualquer: '))

converte = int(input('\nDigite [ 1 ] para converter o número {} para binário;'
                     '\nDigite [ 2 ] para converter o número {} para octal;'
                     '\nDigite [ 3 ] para converter o número {} para hexadecimal.'
                     '\nDigite uma das opções acima: '.format(numero, numero, numero)))

print('-----' * 20)
if converte == 1:
    print('O número {} convertido para BINÁRIO, será igual a: {}'.format(numero, bin(numero)[2:]))
elif converte == 2:
    print('O número {} convertido para OCTAL, será igual a: {}'.format(numero, oct(numero)[2:]))
elif converte == 3:
    print('O número {} convertido para HEXADECIMAL, será igual a: {}'.format(numero, hex(numero)[2:]))
else:
    print('ERRO, OPÇÃO INVÁLIDA!')
