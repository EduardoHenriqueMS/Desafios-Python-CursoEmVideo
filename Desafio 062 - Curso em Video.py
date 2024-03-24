'''
Desafio 61
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''


# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerra quando ele disser que
# quer mostrar 0 termos.

primeiro = int(input("Digite um número inteiro qualquer: "))
razao = int(input("Digite a razão da PA: "))
contador = 1
numero = primeiro
total_termos = 0
mais = 10


while mais != 0:
    total_termos = total_termos + mais
    while contador <= total_termos:
        print(f"{numero}")
        numero += razao
        contador += 1
    mais = int(input("quer mostrar mais alguns termos? Quantos: "))




