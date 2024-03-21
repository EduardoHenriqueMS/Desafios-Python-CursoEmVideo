from random import randint

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

jogador = int(input('''
Escolha:
[0] - Pedra
[1] - Papel
[2] - Tesoura

-> Sua escolha: '''))

print("--------------"*5)

if jogador == 0:
    print("Jogador Escolheu:   PEDRA")
    if computador == 0:
        print("Computador Escolheu:   PEDRA")
    elif computador == 1:
        print("Computador Escolheu:   PAPEL")
    elif computador == 2:
        print("Computador Escolheu:   TESOURA")
elif jogador == 1:
    print("Jogador Escolheu:   PAPEL")
    if computador == 0:
        print("Computador Escolheu:   PEDRA")
    elif computador == 1:
        print("Computador Escolheu:   PAPEL")
    elif computador == 2:
        print("Computador Escolheu:   TESOURA")
elif jogador == 2:
    print("Jogador Escolheu:   TESOURA")
    if computador == 0:
        print("Computador Escolheu:   PEDRA")
    elif computador == 1:
        print("Computador Escolheu:   PAPEL")
    elif computador == 2:
        print("Computador Escolheu:   TESOURA")

else:
    print("Erro! Resposta inválida!")

print("--------------"*5)

if computador == jogador:
    print("EMPATE!")

elif computador == 0:
    if jogador == 1:
        print("Jogador VENCEU!")
    elif jogador == 2:
        print("Jogador PERDEU!")

elif computador == 1:
    if jogador == 0:
        print("Jogador PERDEU!")
    elif jogador == 2:
        print("Jogador VENCEU!")

elif computador == 2:
    if jogador == 0:
        print("Jogador VENCEU!")
    elif jogador == 1:
        print("Jogador PERDEU!")


