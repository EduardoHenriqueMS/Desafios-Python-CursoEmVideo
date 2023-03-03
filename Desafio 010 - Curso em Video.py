# Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar.
# Considere -> US$ 1,00 = R$ 5,20

cart = float(input('Informe quanto dinheiro você tem disponível em reais:'))

dol = cart / 5.20

print('A quantia de R$ {} pode proporcionar um valor de US$ {}'.format(cart, dol))


