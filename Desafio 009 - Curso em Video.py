# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada.

num = int(input('Digite um número:'))

tab1 = num * 1
tab2 = num * 2
tab3 = num * 3
tab4 = num * 4
tab5 = num * 5
tab6 = num * 6
tab7 = num * 7
tab8 = num * 8
tab9 = num * 9
tab10 = num * 10

print('\n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}'.format(tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10))

# Outra variação que eu fiz mais formatada

num = int(input('Digite um número:'))

print('{} x {} = {}'.format(num, 1, num * 1))
print('{} x {} = {}'.format(num, 2, num * 2))
print('{} x {} = {}'.format(num, 3, num * 3))
print('{} x {} = {}'.format(num, 4, num * 4))
print('{} x {} = {}'.format(num, 5, num * 5))
print('{} x {} = {}'.format(num, 6, num * 6))
print('{} x {} = {}'.format(num, 7, num * 7))
print('{} x {} = {}'.format(num, 8, num * 8))
print('{} x {} = {}'.format(num, 9, num * 9))
print('{} x {} = {}'.format(num, 10,num * 10))
