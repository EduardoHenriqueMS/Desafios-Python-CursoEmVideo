# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

numero = int(input("Digite qualquer número inteiro: "))
contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print("\33[33m")
        contador += 1
    else:
        print("\33[31m")
    print(f"{i}")

print("-------"*10)

print(f"O número {numero} foi divisível {contador} vezes")

print("-------"*10)

if contador == 2:
    print(f"O número {numero} é PRIMO!")
else:
    print(f"O número {numero} NÃO É PRIMO!")

