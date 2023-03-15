# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de
# até 200KM e R$0,45 para viagens mais longas.

distancia = int(input('Digite a distancia total em KM, que você percorrerá em sua viagem: '))

if distancia <= 200:
    valor1 = distancia * 0.50
    print('O percurso total é menor ou igual a 200KM!'
          'Então, o preço da passagem a ser paga é de: R${:.2f}'.format(valor1))
else:
    valor2 = distancia * 0.45
    print('O percurso total é maior que 200KM!'
          'Então, o preço da passagem a ser paga é de: R${:.2f}'.format(valor2))
