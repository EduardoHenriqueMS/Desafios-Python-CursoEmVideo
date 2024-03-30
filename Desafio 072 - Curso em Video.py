# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte. Seu programa deverá ler um número pelo
# teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
         "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
         "dezenove", "vinte")

resposta = int(input("Digite um número entre 0 e 20: "))

print("------"*10)

while True:
    if resposta < 0 or resposta > 20:
        resposta = int(input("Número Incorreto! Digite novamente um número entre 0 e 20: "))
    else:
        print(f"Você digitou o número {tupla[resposta]}")
        break