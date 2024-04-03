# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temporario = []
principal = []
maior = menor = 0

while True:
    temporario.append(str(input("Nome: ")))
    temporario.append(float(input("Peso: ")))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input("Quer continuar? [S/N]: ")).upper()
    if resposta == "N":
        break

print("-----"*20)
print(f"Foram cadastradas {len(principal)} pessoas.")
print(f"O maior peso foi de {maior}Kg. Peso de ", end="")
for peso in principal:
    if peso[1] == maior:
        print(f"[{peso[0]}]", end="")
print(f"\nO menor peso foi de {menor}Kg, Peso de ", end="")
for peso in principal:
    if peso[1] == menor:
        print(f"[{peso[0]}]", end="")
