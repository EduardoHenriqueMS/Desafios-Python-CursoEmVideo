# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados.
# Exemplo:
#       Digite um número: 1834
#       unidade: 4
#       dezena: 3
#       centena: 8
#       milhar: 1

numero = int(input('Escreva um número de 0 a 9999: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

unidade = print('A unidade do número {} é {}'.format(numero, u))
dezena = print('A dezena do número {} é {}'.format(numero, d))
centena = print('A centena do número {} é {}'.format(numero, c))
milhar = print('A milhar do número {} é {}'.format(numero, m))




