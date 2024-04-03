# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

lista = list()
nome_mulheres = list()
lista_idade = list()
lista_acima_media = list()

resposta = "S"

while resposta == "S":
    dicionario = {"nome": str(input("Nome: "))}
    dicionario["sexo"] = str(input("Sexo: [M/F] ")).upper()[0]
    if dicionario["sexo"] == "F":
        nome_mulheres.append(dicionario.copy()["nome"])
    while dicionario["sexo"] != "M" and dicionario["sexo"] != "F":
        dicionario["sexo"] = str(input("ERRO! Por favor, digite apenas M ou F. ")).upper()[0]
        if dicionario["sexo"] == "F":
            nome_mulheres.append(dicionario.copy()["nome"])

    dicionario["idade"] = int(input("Idade: "))

    lista_idade.append(dicionario.copy()["idade"])
    lista.append(dicionario.copy())

    print("------"*10)
    resposta = str(input("Quer continuar? [S/N]: ")).upper()[0]
    print("------"*10)

    if resposta == "N":
        break
    while resposta != "S" and resposta != "N":
        resposta = str(input("ERRO! Responda apenas S ou N.")).upper()[0]

print(f"Ao todo temos {len(lista)} pessoas cadastradas.")

media_idade = round(sum(lista_idade)/len(lista_idade))
print(f"A média de idade é de {media_idade}")

print(f"As mulheres cadastradas foram {nome_mulheres}")

print("------"*10)
print("Lista das pessoas que estão acima ou iguais a média de idade: ")
for pessoa in lista:
    if pessoa["idade"] >= media_idade:
        print("      ", end="")
        for k, v in pessoa.items():
            print(f"{k} = {v}; ", end="")
        print()
