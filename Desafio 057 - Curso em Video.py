# Faça um programa que leia o sexo de uma pessoa, mas só aceite
# os valores "M" ou "F". Caso esteja errado, peça a digitalização
# novamente até ter um valor correto.

sexo = str(input("Sexo - [M/F]: ")).upper()

while sexo != "M" and sexo != "F":
    sexo = str(input("Sexo - [M/F]: ")).upper()



