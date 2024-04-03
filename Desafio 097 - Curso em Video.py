# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~

lista = list()

def escreva(msg):

    decoracao = "~" * len(msg)
    print(decoracao)
    print(msg)
    print(decoracao)
    print()

for numero in range(0, 3):
    mensangem = str(input("Digite uma mensagem: "))
    lista.append(mensangem)
    numero += 1

print("--------"*10)

for indice in range(0, 3):
    escreva(lista[indice])