# Modifique as funções que form criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from Desafio109 import Desafio109_moeda

preco = float(input("Digite o preço R$"))
print(f"A metade de {Desafio109_moeda.moeda(preco)} é {Desafio109_moeda.metade(preco, True)}")
print(f"O dobro de {Desafio109_moeda.moeda(preco)} é {Desafio109_moeda.dobro(preco, True)}")
print(f"Aumentando 10%, temos {Desafio109_moeda.aumentar(preco, True)}")
print(f"Reduzindo 13%, temos {Desafio109_moeda.reduzir(preco, True)}")
