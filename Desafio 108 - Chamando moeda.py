# Adapte o código do desafio #107, criando uma função adicional
# chamada moeda() que consiga mostrar os números como um valor
# monetário formatado.

from Desafio108 import Desafio108_moeda

preco = float(input("Digite o preço R$"))
print(f"A metade de {Desafio108_moeda.moeda(preco)} é {Desafio108_moeda.moeda(Desafio108_moeda.metade(preco))}")
print(f"O dobro de {Desafio108_moeda.moeda(preco)} é {Desafio108_moeda.moeda(Desafio108_moeda.dobro(preco))}")
print(f"Aumentando 10%, temos {Desafio108_moeda.moeda(Desafio108_moeda.aumentar(preco))}")
print(f"Reduzindo 13%, temos {Desafio108_moeda.moeda(Desafio108_moeda.reduzir(preco))}")