# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa
# tem que realizar três contagens através da função criada:

from time import sleep

def contador(i, f, p):
    print(f"Contagem de {i} até {f} de {p} em {p}")

    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=" ")
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=" ")
            sleep(0.5)
            cont -= p
        print("FIM!")

contador(1,10, 1)
print("======"*7)
contador(10,0, 2)
print("======"*7)
print("Agora é sua vez!")
contador(i = int(input("Inicio: ")), f = int(input("Fim: ")), p = int(input("Passo: ")))
print("======"*7)