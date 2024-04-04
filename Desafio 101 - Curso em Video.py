# Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.

from datetime import date

def voto():
    ano = int(input("Digite o seu ano de nascimento: "))

    ano = (date.today().year) - ano

    if ano < 16:
        print(f"Com {ano} anos: NÃO VOTA")
    elif ano >= 16 and ano <= 17:
        print(f"Com {ano} anos: VOTO OPCIONAL")
    elif ano > 17 and ano <= 70:
        print(f"Com {ano} anos: VOTO OBRIGATÓRIO")
    elif ano > 70:
        print(f"Com {ano} anos: VOTO OPCIONAL")

print("-----"*10)
voto()
