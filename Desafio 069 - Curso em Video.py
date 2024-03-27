# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

contador_pessoas_18 = 0
homens_cadastrados = 0
mulheres_menos_20 = 0

nome = str(input("NOME: ")).upper().split()
idade = int(input("IDADE: "))
sexo = str(input("SEXO - [M]/[F]: ")).upper()

print("-----"*10)

resposta = str(input("Quer continuar os cadastros? [S] ou [N]: ")).upper()

if idade > 18:
    contador_pessoas_18 += 1

if sexo == "M":
    homens_cadastrados += 1

if sexo == "F" and idade < 20:
    mulheres_menos_20 += 1

while True:
    if resposta == "N":
        break
    if resposta == "S":
        print("-----" * 10)
        nome = str(input("NOME: ")).upper().split()
        idade = int(input("IDADE: "))
        sexo = str(input("SEXO - [M]/[F]: ")).upper()
        print("-----" * 10)
        resposta = str(input("Quer continuar os cadastros? [S] ou [N]: ")).upper()

        if idade > 18:
            contador_pessoas_18 += 1

        if sexo == "M":
            homens_cadastrados += 1

        if sexo == "F" and idade < 20:
            mulheres_menos_20 += 1

print("-----"*10)
print(f"Temos {contador_pessoas_18} pessoas com mais de 18 anos de idade.")
print(f"Temos {homens_cadastrados} homens cadastrados.")
print(f"Temos {mulheres_menos_20} mulheres com menos de 20 anos de idade.")