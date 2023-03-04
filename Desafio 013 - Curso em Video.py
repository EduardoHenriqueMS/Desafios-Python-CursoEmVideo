# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o seu salário:'))

aumen = salario * (115/100)

print('O seu salário é {} e o seu novo salário passará a ser {:.2f}'.format(salario, aumen))
