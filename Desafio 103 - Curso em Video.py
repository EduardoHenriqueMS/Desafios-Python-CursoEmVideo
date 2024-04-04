# Faça um programa que tenha uma função chamada ficha(), que receba
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele
# marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def partida(jogador="<Desconhecido>", gols = 0):
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato")

jogador = input("Nome: ")
gol = input("Gols: ")

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if jogador.strip() == "":
    print("======" * 9)
    partida(gols=gol)
else:
    print("======"*9)
    partida(jogador, gol)


