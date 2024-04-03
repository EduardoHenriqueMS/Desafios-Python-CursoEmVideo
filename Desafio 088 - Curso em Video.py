# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

print("      JOGO DA MEGA SENA      ")
print("-----"*7)

from random import randint

lista_numeros = []

for listas in range(1, 11):
    for numeros in range(0, 6):
        numero_aleatorio = randint(0, 60)
        if numero_aleatorio not in lista_numeros:
            lista_numeros.append(numero_aleatorio)
            numeros += 1
    lista_numeros.sort()
    print(f"Jogo {listas}: {lista_numeros}")
    lista_numeros.clear()
    listas += 1

print("-----"*7)
