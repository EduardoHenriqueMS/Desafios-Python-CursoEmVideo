# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre
# o conteúdo das três listas geradas.

lista_completa = list()
lista_pares = list()
lista_impares = list()
resposta = "S"

while resposta == "S":
    numero = int(input("Digite um número: "))
    print("-----" * 10)
    if numero in lista_completa:
        print("Tente novamente! Número repetido!")
        print("-----" * 10)
    else:
        lista_completa.append(numero)
        if numero % 2 == 0:
            lista_pares.append(numero)
        if numero % 2 == 1 or numero == 1:
            lista_impares.append(numero)
    resposta = str(input("Deseja continuar? [S/N]: ")).upper()
    print("-----" * 10)

print(f"Lista completa -> {lista_completa}")
print(f"Lista de pares -> {lista_pares}")
print(f"Lista de ímpares -> {lista_impares}")