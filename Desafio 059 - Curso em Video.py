# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso

n1 = float(input("Digite um valor: "))
n2 = float(input("Digite um outro valor: "))

lista = [n1, n2]

operacao = 0

resposta = 0

while resposta != 5:
    resposta = int(input('''
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa
    -> Resposta: '''))
    if resposta == 1:
        operacao = n1 + n2
        print(f"SOMA = {operacao}")
    elif resposta == 2:
        operacao = n1 * n2
        print(f"MULTIPLICAÇÃO: {operacao}")
    elif resposta == 3:
        print(f"O maior valor é: {max(lista)}")
    elif resposta == 4:
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite um outro valor: "))
    elif resposta < 1 and resposta > 5:
        print("Erro! Opção Inválida!")

print("------" * 10)

print("FIM DO PROGRAMA!")