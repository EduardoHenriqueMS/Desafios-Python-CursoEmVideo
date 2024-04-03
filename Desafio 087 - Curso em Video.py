# Aprimore o desafio 086, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

contas_pares = []

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um número para [{linha}, {coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            contas_pares.append(matriz[linha][coluna])

print("-----"*10)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()

print("-----"*10)
print(f"A soma de todos os valores pares digitados é = {sum(contas_pares)}")
print(f"A soma dos valores da terceira coluna é = {matriz[0][2] + matriz[1][2] + matriz[2][2]}")
print(f"O maior valor da segunda linha é = {max(matriz[1])}")