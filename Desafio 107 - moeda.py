# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
# e use algumas dessas funções.

def metade(numero=0):
    return numero/2

def dobro(numero=0):
    return numero*2

def aumentar(numero=0):
    return (numero + (numero*10/100))

def reduzir(numero=0):
    return (numero - (numero*13/100))
