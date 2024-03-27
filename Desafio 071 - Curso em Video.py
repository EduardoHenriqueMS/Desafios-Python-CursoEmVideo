# Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.

# OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input("Digite a quantia que você deseja sacar: R$"))

total = valor

cedulas = 50

total_cedula = 0

while True:
    if total >= cedulas:
        total -= cedulas
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f"Total de {total_cedula} cédulas de R${cedulas}")
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedula = 0
        if total == 0:
            break



