# Crie um pequeno sistema modularização que permita cadastrar pessoas
# pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar
# todas as pessoas cadastradas

def leiaint(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaint("\033[32mSua Opção: \033[m")
    return opc