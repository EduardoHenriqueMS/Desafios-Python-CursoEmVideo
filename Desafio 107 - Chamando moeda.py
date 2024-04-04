# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
# e use algumas dessas funções.

from Desafio107 import Desafio107_moeda

preco = float(input("Digite o preço R$"))
print(f"A metade de {preco} é {Desafio107_moeda.metade(preco)}")
print(f"O dobro de {preco} é {Desafio107_moeda.dobro(preco)}")
print(f"Aumentando 10%, temos {Desafio107_moeda.aumentar(preco)}")
print(f"Reduzindo 13%, temos {Desafio107_moeda.reduzir(preco)}")