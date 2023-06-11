# Escreva um programa para aprovar o empréstimo bancário para a compra de uma
# casa. O programa vai perguntar o 'valor da casa', o 'salário' do comprador e
# em 'quantos anos' ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
# salário ou então o empréstimo será negado.
from time import sleep

casa = float(input('Digite o preco da casa que será comprada: '))

salario = float(input('Digite o salário do comprador da casa: '))

anos = int(input('Digite em quantos anos o comprador espera pagar a dívida: '))
meses = anos * 12

salario30 = salario * 130/100
prestacao = casa / meses

print('----' * 20)

print('O preço da casa é de R${:.2f};'.format(casa))
print('O salário do comprador da casa é de: R${:.2f}'.format(salario))
print('O comprador espera pagar em {} anos.'.format(anos))

print('----' * 20)
print('PROCESSANDO . . .')
sleep(5)
print('----' * 20)

if prestacao > salario30:
    print('O seu empréstimo foi NEGADO!')
elif prestacao <= salario30:
    print('O valor da prestação a ser paga por mês será de: {:.2f}'.format(prestacao))
else:
    print('ERRO!')
