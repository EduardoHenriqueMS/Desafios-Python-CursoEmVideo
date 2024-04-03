# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura
# e comprimento) e mostre a área do terreno.

def calcula_area():
    c = float(input("Digite o comprimento: "))
    l = float(input("Digite a largura: "))
    print(f"A área de um terreno {c} x {l} é de {c * l} metros quadrados.")

calcula_area()