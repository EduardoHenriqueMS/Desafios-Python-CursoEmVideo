# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma
# uma área de 2m^2.

lar = float(input('Digite a largura da parede em metros:'))
alt = float(input('Digite a altura da parede em metros:'))

area = lar * alt

quant = area / 2

print('A área da parede é:  {} metros quadrados'.format(area))
print('A quantidade de tinta necessária para pintar a parede é:  {} litros'.format(quant))

