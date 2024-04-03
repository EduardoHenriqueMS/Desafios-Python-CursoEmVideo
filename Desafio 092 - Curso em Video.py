# Crie um programa que leia nome, ano de nascimento e carteira
# de trabalho e cadastre-o (com idade) em um dicionário. Se por
# acaso a CTPS for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.

from datetime import date

dicionario = {"nome": str(input("Nome: ")),
              "idade": int(input("Ano de Nascimento: ")),
              "carteira": int(input("Carteira de Trabalho (0 não tem): "))}

ano_nascimento = dicionario.copy()["idade"]
dicionario["idade"] = date.today().year - dicionario["idade"]

if dicionario["carteira"] != 0:
    dicionario["contratacao"] = int(input("Digite o ano de contratação: "))
    dicionario["salario"] = float(input("Salário: R$"))
    idade_aposentadoria = (dicionario["contratacao"] - ano_nascimento) + 35
    dicionario["aposentadoria"] = idade_aposentadoria

print("======="*6)

for key, valor in dicionario.items():
    print(f"  - {key} tem o valor {valor}")