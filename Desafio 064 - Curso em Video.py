# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numeros = 0
contador_numeros = 0
soma_numeros = 0

numeros = int(input("Digite um número inteiro qualquer [999 para parar]: "))
while numeros != 999:
    contador_numeros += 1
    soma_numeros += numeros
    numeros = int(input("Digite um número inteiro qualquer: "))

print(f"Você digitou {contador_numeros} números e a soma deles é {soma_numeros}")

