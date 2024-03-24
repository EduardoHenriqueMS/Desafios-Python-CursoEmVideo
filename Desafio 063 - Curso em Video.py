# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
# primeiros elementos de uma Sequência de Fibonacci
# Ex.: 0->1->1->2->3->5->8

inteiro = int(input("Digite um número inteiro qualquer: "))

contador = 1

antes = 0
depois = 1
resposta = 0

print("A Sequência de Fibonacci ficará assim:")

while contador <= inteiro:
    print(f"{resposta}")
    resposta = antes + depois
    antes = depois
    depois = resposta
    contador += 1