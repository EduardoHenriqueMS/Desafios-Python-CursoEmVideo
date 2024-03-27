# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que
# é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).

numeros = int(input("Digite um número inteiro qualquer [999 para parar]: "))

soma_numeros = 0
contador = 0

while True:
    if numeros == 999:
        break
    contador += 1
    soma_numeros += numeros
    numeros = int(input("Digite um número inteiro qualquer [999 para parar]: "))

print("------"*10)
print(f"Foram digitados {contador} números e a soma deles foi {soma_numeros}")