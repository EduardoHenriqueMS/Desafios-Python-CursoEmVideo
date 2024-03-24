# Melhore o jogo do Desafio 28 onde o computador vai "pensar" em um número de 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint
contador_jogadas = 0
jogador = "a"
computador = "b"

while jogador != computador:
    if jogador != computador:
        jogador = int(input("Pense em um número de 0 a 10: "))
        computador = randint(0, 10)
        print(f"Computador pensou em {computador}")
        contador_jogadas += 1
    print("------" * 10)

print(f"Você conseguiu acertar em {contador_jogadas} jogadas, PARABÉNS!")

