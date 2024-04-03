# Faça um programa que leia nome e média de um aluno, guardando
# também a situação em um dicionário. No final, mostre o conteúdo
# da estrutura na tela.

dicionario = dict()

dicionario["nome"] = str(input("Nome: "))
dicionario["nota"] = float(input("Nota: "))

print("-----"*6)

if dicionario["nota"] < 5.0:
    dicionario["status"] = "Reprovado"
elif dicionario["nota"] >= 5.0 and dicionario["nota"] < 7.0:
    dicionario["status"] = "Recuperação"
else:
    dicionario["status"] = "Aprovado"

for k, v in dicionario.items():
    print(f"  - {k} é igual a {v}")