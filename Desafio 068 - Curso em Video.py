# Faça um programa que jogue par ou ímpar com o computador. O jogo será
# interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint

print("======Jogo do PAR ou ÌMPAR======")
escolha = str(input("[P] ou [I]: ")).upper()
jogador = 0
computador = 0
total = 0
contador_vitorias = 0

while True:
    if escolha == "P":
        jogador = int(input("Escolha um número: "))
        print("------" * 10)
        computador = randint(0, 10)
        total = jogador + computador
        if total % 2 == 0:
            print(f"Jogador jogou {jogador} e computador {computador}. Total deu {total}")
            print("VOCÊ VENCEU!")
            print("Vamos jogar novamente . . . ")
            print("------"*10)
            total = 0
            contador_vitorias += 1
            escolha = str(input("[P] ou [I]: ")).upper()
        elif total % 2 == 1:
            print(f"Jogador jogou {jogador} e computador {computador}. Total deu {total}")
            print("VOCÊ PERDEU!")
            break
    elif escolha == "I":
        jogador = int(input("Escolha um número: "))
        computador = randint(0, 10)
        total = jogador + computador
        if total % 2 == 1:
            print(f"Jogador jogou {jogador} e computador {computador}. Total deu {total}")
            print("VOCÊ VENCEU!")
            print("Vamos jogar novamente . . . ")
            print("------" * 10)
            total = 0
            contador_vitorias += 1
            escolha = str(input("[P] ou [I]: ")).upper()
        elif total % 2 == 0:
            print(f"Jogador jogou {jogador} e computador {computador}. Total deu {total}")
            print("VOCÊ PERDEU!")
            break

print("------"*10)
print(f"Você VENCEU o computador {contador_vitorias} vez(es)")
