# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date

atual = date.today().year

soma_maioridade = 0
soma_menor = 0

for pessoa in range(1, 8):
    nome = str(input("Digite o nome da pessoa: "))
    ano = int(input("Digite o ano de aniversário da pessoa: "))
    if atual - ano >= 18:
        print(f"{nome} atingiu a maioridade!")
        soma_maioridade += 1
    else:
        print(f"{nome} ainda é menor de idade!")
        soma_menor += 1
    print("-------"*10)

print(f"Total de pessoas que atingiram a maioridade = {soma_maioridade}")
print(f"Total de pessoas que ainda são menores de idade = {soma_menor}")

