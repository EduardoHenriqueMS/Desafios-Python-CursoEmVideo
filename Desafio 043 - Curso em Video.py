# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso.
# Entre 18.5 e 25: Peso ideal.
# 25 até 30: Sobrepeso.
# 30 até 40: Obesidade.
# Acima de 40: Obesidade Mórbida.

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

status = peso / (altura ** 2)

print('O seu status é: {:.2f}'.format(status))

print('---' * 20)

if status < 18.5:
    print('Abaixo do peso!')
elif status >= 18.5 and status < 25:
    print('Peso ideal!')
elif status >= 25 and status < 30:
    print('Sobrepeso!')
elif status >= 30 and status < 40:
    print('Obesidade!')
elif status > 40:
    print('Obesidade mórbida!')
else:
    print('ERRO!')
