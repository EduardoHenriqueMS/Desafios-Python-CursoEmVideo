from random import randint

lista = list()

def valores():
    for n in range(0, 5):
        sorteio = randint(1, 10)
        lista.append(sorteio)
        n += 1

    print(f"Sorteando 5 valores da lista {lista} PRONTO!")

def soma():
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(f"Somando os valores pares de {lista}, temos {soma}")

valores()
soma()