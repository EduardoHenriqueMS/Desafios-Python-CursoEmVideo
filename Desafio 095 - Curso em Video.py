# Crie um programa que gerencie o aproveitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas partidas
# ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de
# gols feitos durante o campeonato.

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do jogador: "))
    total = int(input(f"Quantes partidas {jogador['nome']} jogou?"))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f"   Quantos gols na partida {c+1}?")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input("Quer continuar? [S/N]: ")).upper()[0]
        if resposta in "SN":
            break
        print("ERRO! Responda apenas S ou N")
    if resposta == "N":
        break
print("------"*10)
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("------"*10)
for k, v in enumerate(time):
    print(f"{k:>3} ",end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("------"*10)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f"    No jogo {i+1} fez {g} gols.")
    print("------"*10)

