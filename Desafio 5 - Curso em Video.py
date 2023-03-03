# Faça um programaque leia um número inteiro e mostre na tela
# o seu sucessor e o seu antecessor.

numero1 = int(input('Digite um número:'))

sucessor = numero1 + 1
antecessor = numero1 - 1

print('\n O antecessor do número {} é {} \n O sucessor do número {} é {}'.format(numero1,sucessor,numero1,antecessor))
