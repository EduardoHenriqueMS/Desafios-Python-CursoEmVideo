# Faça um programa que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário com as seguintes
# informações:
# –Quantidade de notas
# –A maior nota
# –A menor nota
# –A média da turma
# –A situação (opcional)


def notas(*numero, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos(aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = dict()
    dicionario["total"] = len(numero)
    dicionario["maior"] = max(numero)
    dicionario["menor"] = min(numero)
    dicionario["media"] = round(sum(numero)/len(numero))
    if situacao:
        if dicionario["media"] >= 7:
            dicionario["situacao"] = "BOA"
        elif dicionario["media"] >= 5:
            dicionario["situacao"] = "RAZOÁVEL"
        else:
            dicionario["situacao"] = "RUIM"
    return dicionario


resposta = notas(5.5, 2.5, 1.5, situacao=True)
print(resposta)
print("========="*9)
help(notas)