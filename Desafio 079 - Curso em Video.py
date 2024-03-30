# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista = list()
resposta = "S"


while resposta == "S":
    valor = int(input("Digite um valor para adicionar na lista: "))
    print("-----" * 10)
    if valor in lista:
        print("Valor igual ao que está na lista! Por favor ... Tente Novamente")
        print("-----" * 10)
    else:
        lista.append(valor)
    resposta = str(input("Deseja continuar adicionano valores [S/N]: ")).upper()
    print("-----" * 10)

lista.sort()

print(f"Lista em ordem crescente -> {lista}")


