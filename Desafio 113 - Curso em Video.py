# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
# possibilidade da digitação de um número de tipo inválido. Aproveite e crie
# também uma função leiaFloat() com a mesma funcionalidade.

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

def leiafloat(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return n


numero1 = leiaint("Digite um número inteiro: ")
numero2 = leiafloat("Digite um número float: ")

print(f"O número inteiro digitado foi {numero1} e o número real digitado foi {numero2}")
