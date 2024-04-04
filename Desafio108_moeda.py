# Adapte o código do desafio #107, criando uma função adicional
# chamada moeda() que consiga mostrar os números como um valor
# monetário formatado.

def metade(numero=0):
    return numero/2

def dobro(numero=0):
    return numero*2

def aumentar(numero=0):
    return (numero + (numero*10/100))

def reduzir(numero=0):
    return (numero - (numero*13/100))

def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', '.')
