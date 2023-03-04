# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa  R$60 por dia e R$0,15 por Km rodado.

perc = int(input('Escreva a quantidade de Km percorridos pelo carro:'))
alug = int(input('Escreva por quantos dias o carro foi alugado:'))

preco = (alug * 60) + (perc * 0.15)

print('O carro percorreu {} Km e foi alugado por {} dia(s) o preço total do aluguel foi {:.2f}'.format(perc, alug, preco))

