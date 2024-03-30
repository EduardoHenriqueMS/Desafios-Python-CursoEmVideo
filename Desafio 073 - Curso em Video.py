# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time do Vasco.

tupla_time = ("Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo", "Red Bull Bragantino",
              "Fluminense", "Atlético-PR", "Internacional", "Fortaleza", "São Paulo", "Cuiabá",
              "Corinthians", "Cruzeiro", "Vasco", "Bahia", "Santos", "Goiás", "Coritiba", "América-MG")

print("======"*10)
print("Os cinco primeiros colocados, são:")

for time in range(0, 5):
    print(f"-{tupla_time[time]}")

print("======"*10)

print("Os últimos 4 colocados da tabela, são: ")

for ultimos in range(-1, -5, -1):
    print(f"-{tupla_time[ultimos]}")

print("======"*10)

print("Os times em ordem alfabética ficarão assim: ")
organizado = sorted(tupla_time)

for alfabetica in range(0, 20):
    print(f"-{organizado[alfabetica]}")

print("======"*10)

posicao_vasco = tupla_time.index("Vasco") + 1

print(f"O time do {tupla_time[posicao_vasco - 1]} está na posição: {posicao_vasco}")

print("======"*10)