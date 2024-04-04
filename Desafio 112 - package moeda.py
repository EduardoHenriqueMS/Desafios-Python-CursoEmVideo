# Desafio 112 - package 'moeda'
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
# chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
# funcionar como a função imputa(), mas com uma validação de dados para aceitar
# apenas valores que seja monetários.

def metade(numero=0, format=False):
    dividido= numero/2
    return dividido if format is False else moeda(dividido)

def dobro(numero=0, format=False):
    dobrado = numero * 2
    return dobrado if format is False else moeda(dobrado)

def aumentar(numero=0, format=False):
    aumento = (numero + (numero * 10 / 100))
    return aumento if format is False else moeda(aumento)

def reduzir(numero=0, format=False):
    reduzida = (numero - (numero*13/100))
    return reduzida if format is False else moeda(reduzida)

def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', '.')

def resumo(numero=0):
    print("="*30)
    print("RESUMO DO VALOR".center(30))
    print("="*30)
    print(f"Preço analisado: \t{moeda(numero)}")
    print(f"Dobro do preco: \t{dobro(numero, True)}")
    print(f"Metade do preço: \t{metade(numero, True)}")
    print(f"{round(aumentar(numero))}% de aumento: \t{aumentar(numero, True)}")
    print(f"{round(reduzir(numero))}% de redução: \t{reduzir(numero, True)}")
    print("=" * 30)