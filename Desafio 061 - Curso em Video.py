# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input("Digite um número inteiro qualquer: "))
razao = int(input("Digite a razão da PA: "))
contador = 0


while contador < 10:
    print(primeiro)
    primeiro += razao
    contador += 1



