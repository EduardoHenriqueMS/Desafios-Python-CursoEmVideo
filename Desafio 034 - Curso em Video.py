# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('Digite o valor do seu salário: '))

if salario <= 1250:
    aumento1 = salario * (115/100)
    #aumento1 = salario + (salario * 15/100)           -> OUTRA FORMA
    print('A pessoa que ganha menos ou igual R$1250,00 terá o seu salário de R${:.2f} ajustado para: R${:.2f}'.format(salario, aumento1))

else:
    aumento2 = salario * (110/100)
    #aumento2 = salario + (salario * 15/100)
    print('A pessoa que ganha mais que R$1250,00 terá o seu salário de R${:.2f} ajustado para: R${:.2f}'.format(salario, aumento2))
