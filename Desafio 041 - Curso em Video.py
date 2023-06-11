# A Confederação Nacional de natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

idade = int(input('Digite a sua idade: '))

if idade <= 9:
    print('A sua categoria é a MIRIM!')
elif idade >= 10 and idade <= 14:
    print('A sua categoria é a INFANTIL!')
elif idade >= 15 and idade <= 19:
    print('A sua categoria é a JÚNIOR!')
elif idade == 20:
    print('A sua categoria é a SÊNIOR!')
else:
    print('A sua categoria é a MASTER!')
