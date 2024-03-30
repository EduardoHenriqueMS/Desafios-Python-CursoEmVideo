# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

lista = list()
contador_numero_nove = 0

print("======"*8)

for numeros in range(0,4):
    numeros = int(input("Digite qualquer número inteiro entre 0 e 10: "))
    if numeros < 0 or numeros > 10:
        numeros = int(input("Número incorreto, digite novamente: "))
    lista.append(numeros)
    if numeros == 9:
        contador_numero_nove += 1

tupla = (lista[0], lista[1], lista[2], lista[3])

print("------"*10)

print("Os valores dentro da tupla, são: ")
for i in range(0, 4):
    print(f"-> {tupla[i]}")

print("------"*10)

print(f"O número 9 aparaceu {contador_numero_nove} vezes")

print("------"*10)

if 3 in tupla:
    print(f"O primeiro valor 3, foi digitado na posição {tupla.index(3) + 1}")
else:
    print("O valor 3 não foi digitado!")

print("------"*10)

print("Os números pares são: ")
for pares in tupla:
    if pares % 2 == 0:
        print(f"-> {pares}")

print("======"*8)