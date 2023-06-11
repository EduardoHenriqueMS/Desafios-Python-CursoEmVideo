# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade:
# -Se ele ainda vai se alistar ao serviço militar.
# -Se é a hora de se alistar.
# -Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite o seu ano de nascimento: '))
data = date.today().year - ano
if data < 18:
    print('Você ainda não possuí idade suficiente para se alistar.')
    tempo = 18 - data
    print('Faltam {} ano(s) para você se alistar!'.format(tempo))
elif data == 18:
    print('Você está na idade de alistamento!')
elif ano > 18:
    print('Você já passou do tempo de alistamento!')
    tempo1 = data - 18
    print('O prazo de alistamento era até 18 anos, você passou do prazo em: {} ano(s).'.format(tempo1))
else:
    print('ERRO!')
