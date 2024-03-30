# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e
# o maior valor que estão na tupla.

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))

print(f"Tupla = {numeros}")

print("------"*10)

print("Os números gerados foram: ")
for i in range(0, 5):
    print(f"-> {numeros[i]}")

oraganizados = sorted(numeros)

print("------"*10)

print(f"O maior número é {oraganizados[-1]}")
print(f"O menor número é {oraganizados[0]}")