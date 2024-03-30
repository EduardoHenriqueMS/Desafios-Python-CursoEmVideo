# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()

for i in range(0, 5):
    valor = int(input("Digite um valor: "))
    if i == 0 or valor> lista[-1]:
        lista.append(valor)
        print("Adicionando valor ao final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f"Adicionando na posição {pos} da lista...")
                break
            pos += 1

print("-----"*10)

print(f"Lista em ordem crescente -> {lista}")


