# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

lista = list()


for i in range(0, 5):
    lista.append(int(input("Digite qualquer número inteiro: ")))

print("------"*10)
print(f"Lista -> {lista}")
print("------"*10)
print(f"O maior valor da lista é {max(lista)} e ele está na posição {lista.index(max(lista))+1}")
print(f"O menor valor da lista é {min(lista)} e ele está na posição {lista.index(min(lista))+1}")