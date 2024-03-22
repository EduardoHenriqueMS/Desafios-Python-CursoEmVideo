# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso
# lidos.

lista = list()

for i in range(1, 6):
    nome = str(input("Digite o seu nome: "))
    peso = float(input("Digite o seu peso em KG: "))
    print("------"*10)
    lista.append(peso)

print(f"O peso máximo é: {max(lista)}")
print(f"O peso mínimo é: {min(lista)}")