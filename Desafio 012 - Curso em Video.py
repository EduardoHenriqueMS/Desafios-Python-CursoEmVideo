# Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto.

pre = float(input('Digite o preço do produto:'))
desc = pre * (95/100)

print('O preço do produto é {:.2f}, mas com 5% de desconto ficará {:.2f}'.format(pre, desc))

