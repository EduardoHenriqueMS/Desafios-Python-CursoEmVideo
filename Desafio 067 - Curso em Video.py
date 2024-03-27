# Faça um programa que mostre a tabuada de vários números, um de cada vez
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.

num = int(input("Você quer ver a tabuada de qual valor? "))
contador = 0

while True:
    if num < 0:
        break
    elif contador != 11:
        print(f"{num} x {contador} = {num*contador}")
        contador += 1
        if contador == 11:
            contador = 0
            print("-----" * 10)
            print("Digite qualquer número negativo para sair!")
            num = int(input("Você quer ver a tabuada de qual valor? "))


