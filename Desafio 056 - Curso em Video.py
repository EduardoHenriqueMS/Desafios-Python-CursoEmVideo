# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

soma_idade = 0
homem_mais_velho = 0
nome_velho = ""
mulheres_menor_20 = 0

for i in range(1, 5):
    print(f"PESSOA {i}")
    nome = str(input("Digite o seu nome: ")).strip()
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Sexo [M/F]: ").upper())
    print("------"*10)
    soma_idade += idade

    if i==1 and sexo=="M":
        homem_mais_velho = idade
        nome_velho = nome
    if sexo=="M" and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_velho = nome
    if sexo == "F" and idade < 20:
        mulheres_menor_20 += 1

print(f"A média de idade do grupo é {soma_idade/4}")
print(f"o nome do homem mais velho é {nome_velho} e sua idade é {homem_mais_velho}")
print(f"Existem {mulheres_menor_20} mulheres que têm menos de 20 anos nesse programa")