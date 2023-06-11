# Escreva um programa que leia 'dois números' inteiros e compare-os, mostrando
# na tela uma mensagem:
# O primeiro valor é 'maior'.
# O segundo valor é 'maior'.
# 'NÃO EXISTE' valor maior, os dois são iguais.

numero1 = int(input('Digite um número inteiro qualquer: '))
numero2 = int(input('Digite um outro número inteiro qualquer: '))

print('----' * 20)

if numero1 > numero2:
    print('O primeiro valor = {} -> É MAIOR!'.format(numero1))
elif numero2 > numero1:
    print('O segundo valor = {} -> É MAIOR!'.format(numero2))
elif numero1 == numero2:
    print('O primeiro valor é igual ao segundo valor')
else:
    print('ERRO, OPÇÃO INVÁLIDA!')
