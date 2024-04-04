# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
# chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
# funcionar como a função imputa(), mas com uma validação de dados para aceitar
# apenas valores que seja monetários.

from Desafio112.utilidadescev import moeda
from Desafio112.utilidadescev import dado

preco = dado.leiaDinheiro("Digite o preço: R$")
moeda.resumo(preco)