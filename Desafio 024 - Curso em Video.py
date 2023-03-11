# Crie um programa que leia o nome de uma cidade e diga se
# ela começa ou não com o nome "SANTO".

nome = str(input('Digite o nome da cidade: ')).upper()

lista = nome.split()
variavel = 'SANTO' in lista[0]

print('O nome da cidade {} começa com a palavra SANTO? {}'.format(nome, variavel))

