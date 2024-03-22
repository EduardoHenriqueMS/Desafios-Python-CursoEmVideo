# Refaça o Desafio 009 mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando laço for

usuario = int(input("Digite um número inteiro qualquer para saber sua tabuada: "))

for tabuada in range(0, 11):
    print(f"{tabuada} X {usuario} = {usuario*tabuada}")