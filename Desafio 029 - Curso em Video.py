# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

from time import (sleep)

velocidade = int(input('Digite a velocidade atual do seu veículo: '))

if velocidade <= 80:
    print('O seu veículo está dentro da velocidade permitida!')

else:
    print('O seu veículo ultrapassou a velocidade permitida!')

    print('---' * 40)
    print('CALCULANDO A MULTA . . .')
    print('---' * 40)
    sleep(3)

    multa = (velocidade - 80) * 7
    print('A multa a ser paga é de R$ {:.2f}'.format(multa))
