# Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.

lista = list()
resposta = "S"

def valor(*numeros):
    print("======"*8)
    print("Analisando os valores passados...")
    if lista == [0]:
        print(f"Foram informados {0} valores ao todo.")
    else:
        print(f"{lista} Foram informados {len(lista)} valores ao todo.")
    if len(lista) == 0:
        print(f"O maior valor informado foi {0}")
    elif len(lista) > 0:
        print(f"O maior valor informado foi {max(lista)}")
    lista.clear()

while resposta == "S":
    print("Digite [0] caso deseje não mostrar nenhum número.")
    numero = int(input("Digite os números que deseja mostrar: "))
    lista.append(numero)
    resposta = str(input("Deseja continuar? [S/N]: ")).upper()
    if resposta == "N":
        valor(numero)
        break
