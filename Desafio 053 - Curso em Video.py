# Crie um programa que leia uma frase qualquer e diga se ela é um políndromo,
# desconsiderando os espaços.

frase = str(input("Digite qualquer frase: ")).strip().upper()

palavras = frase.split()

tudo_junto = "".join(palavras)

inverso = ""

for i in range(len(tudo_junto) - 1, -1, -1):
    inverso += tudo_junto[i]

if inverso == tudo_junto:
    print("PALÍNDROMO!")
else:
    print("NÃO É UM PALÍNDROMO!")


