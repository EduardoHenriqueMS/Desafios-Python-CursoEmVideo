# Crie um porgrama que leia o nome de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final, mostre:
# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de R$1000.
# c) Qual é o nome do produto mais barato.

print("____-CARRINHO-____")

nome = str(input("Nome do produto: "))
produto = float(input("Preço do produto: "))
contador_produto_mais_de_1000 = 0
contador = 0
menor = 0
barato = ""

lista = list()
lista.append(produto)

if produto > 1000:
    contador_produto_mais_de_1000 += 1

print("------"*10)
resposta = str(input("Quer continuar adicionando produtos? [S]/[N]: ")).upper()
print("------" * 10)

while True:
    contador += 1
    if contador == 1 or produto < menor:
        menor = produto
        barato = nome

    if resposta == "N":
        break
    if resposta == "S":
        nome = str(input("Nome do produto: "))
        produto = float(input("Preço do produto: "))
        lista.append(produto)

        print("------" * 10)
        resposta = str(input("Quer continuar adicionando produtos? [S]/[N]: ")).upper()
        print("------" * 10)

        if produto > 1000:
            contador_produto_mais_de_1000 += 1


print(f"O total gasto na compra foi R${sum(lista)}")
print(f"O total de produtos que custam mais de R$ 1000,00 é de {contador_produto_mais_de_1000}")
print(f"O nome do produto mais barato é {barato} e ele custa {menor}")