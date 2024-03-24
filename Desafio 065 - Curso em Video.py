# Crie um programa que leia vários números inteiros pelo teclado. No final
# da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.

contador_valores = 0
soma_valores = 0
lista = list()
resposta = "S"

valores = int(input("Digite um número inteiro qualquer: "))
resposta = str(input("Quer continuar o programa [S/N]")).upper()
lista.append(valores)
contador_valores += 1
soma_valores += valores

while resposta != "N":
    valores = int(input("Digite um número inteiro qualquer: "))
    contador_valores += 1
    soma_valores += valores
    lista.append(valores)
    resposta = str(input("Quer continuar o programa [S/N]")).upper()


print("------"*10)
print(f"Você digitou {contador_valores} números.")
print(f"O maior número foi {max(lista)}")
print(f"O menor número foi {min(lista)}")
print(f"A média de todos os valores digitados foi: {soma_valores/contador_valores}")