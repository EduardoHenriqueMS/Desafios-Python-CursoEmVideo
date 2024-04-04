# Adicione o módulo moeda.py criado nos desafios anteriores, uma função
# chamada resumo(), que mostre na tela algumas informações geradas pelas
# funções que já temos no módulo criado até aqui.

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
    print(f"{aumentar(numero)}% de aumento: \t{aumentar(numero, True)}")
    print(f"{reduzir(numero)}% de redução: \t{reduzir(numero, True)}")
    print("=" * 30)