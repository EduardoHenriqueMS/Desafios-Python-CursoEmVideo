# Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e
# ímpares em ordem crescente.

lista = [[], []]


for n in range(0, 7):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        lista[0].append(numero)
    if numero % 2 == 1 or numero == 1:
        lista[1].append(numero)

lista.sort()

print(f"Todos os valores ímpares em ordem crescente: {lista[0]}")
print(f"Todos os valores pares em ordem crescente: {lista[1]}")




