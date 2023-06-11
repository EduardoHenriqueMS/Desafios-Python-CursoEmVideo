# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu 'preço normal' a 'condição de pagamento':
# À vista dinheiro / cheque: 10% de desconto.
# À vista no cartão : 5% de desconto.
# Em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros.

valor = float(input('Digite o valor do produto: '))

print('-----' * 20)
print('Agora vamos ver quais as opções de pagamento e se você tem direito a um desconto!')
print('-----' * 20)

print('Digite [1] caso o pagamento seja feito à vista em DINHEIRO ou CHEQUE.')
print('Digite [2] caso o pagamento seja feito à vista no CARTÃO.')
print('Digite [3] caso o pagamento seja feito em 2x no CARTÃO.')
print('Digite [4] caso o pagamento seja feito 3x ou mais no CARTÃO')

resposta = int(input('A opção selecionada é: '))

if resposta == 1:
    desconto = valor - (valor * 10/100)
    print('O valor do produto era de R${:.2f} e passou a ser de R${:.2f}'.format(valor, desconto))
elif resposta == 2:
    desconto = valor - (valor * 5/100)
    print('O valor do produto era de R${:.2f} e passou a ser de R${:.2f}'.format(valor, desconto))
elif resposta == 3:
    desconto = valor
    print('O valor do produto era de R${:.2f} e passou a ser de R${:.2f}'.format(valor, desconto))
elif resposta == 4:
    juros = (valor * 120/100)
    print('O valor do produto era de R${:.2f} e passou a ser de R${:.2f}'.format(valor, juros))
else:
    print('ERRO! Opção Inválida!')
