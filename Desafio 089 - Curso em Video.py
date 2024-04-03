# Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

lista = []
resposta = "S"

while resposta == "S":
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    resposta = str(input("Deseja continuar? [S/N]: ")).upper()
    lista.append([nome, [nota1, nota2], media])

    if resposta == "N":
        break

print("-----"*6)
print(f'{"N0.":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-----"*6)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print("-" * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f"Notas de {lista[opc][0]} são {lista[opc][1]}")

