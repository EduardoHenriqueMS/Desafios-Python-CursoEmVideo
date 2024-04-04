# Modifique as funções que form criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

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
