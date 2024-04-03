# Crie um programa que gerencie o aproveitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas partidas
# ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de
# gols feitos durante o campeonato.

lista_gols = []

dicionario = {"nome": input("Nome do jogador: ")}

partidas = int(input(f"Quantas partidas {dicionario['nome']} jogou? "))

for numero in range(0, partidas):
    dicionario["gols"] = int(input(f"Quantos gols na partida {numero + 1}? "))
    lista_gols.append(dicionario["gols"])
    numero += 1

total_gols = sum(lista_gols)
dicionario["gols"] = lista_gols
dicionario["total"] = total_gols
print("-=-=-=-="*12)

print(dicionario)

print("-=-=-=-="*12)

for v, k in dicionario.items():
    print(f"O campo {v} tem valor {k}")

print("-=-=-=-="*12)

print(f"O jogador {dicionario['nome']} jogou {partidas} partidas.")

for i, v in enumerate(lista_gols):
    print(f"  => Na partida {i}, fez {v} gols")

print(f"Foi um total de {total_gols} gols.")