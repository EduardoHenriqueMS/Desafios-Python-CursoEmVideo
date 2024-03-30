# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
resposta = "S"
contador = 0

while resposta == "S":
    numero = int(input("Digite um número qualquer: "))
    print("-----" * 10)
    if numero in lista:
        print("Tente novamente! Número repetido!")
        print("-----" * 10)
    else:
        lista.append(numero)
        contador += 1

    resposta = str(input("Deseja continuar? [S/N]: ")).upper()
    print("-----"*10)

print(f"Foram digitados {contador} elementos")
lista.sort(reverse=True)
print(f"Lista em forma decrescente -> {lista}")
if 5 in lista:
    print("O valor 5 foi digitado!")
elif 5 not in lista:
    print("O valor 5 NÃO foi digitado!")


