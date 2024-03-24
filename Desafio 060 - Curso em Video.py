# Faça um programa que leia um número qualquer e mostre o seu fatorial
# Ex.: 5! = 5*4*3*2*1 = 120

from math import factorial

numero = int(input("Digite um número inteiro qualquer: "))

fatorial = factorial(numero)

contador = numero
print(f"{numero}! = ", end="")
while contador > 0:
    print(f"{contador}", end="")
    print(" x " if contador > 1 else " = ", end="")
    contador -= 1

print(fatorial)