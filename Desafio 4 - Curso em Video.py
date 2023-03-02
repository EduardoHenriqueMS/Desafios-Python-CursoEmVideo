# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveís sobre ele.

variavel = input('Escreva algo: ')

print('')
print(('A variavel {} é alfanumérica (possuí apenas letras ou números)?').format(variavel),(variavel.isalnum()))
print('')
print(('A variavel {} contem apenas letras?').format(variavel),(variavel.isalpha()))
print('')
print(('A variavel {} contém todos os caracteres de valor decimal?').format(variavel),(variavel.isdecimal()))
print('')
print(('A variavel {} é categorizada como um dígito decimal?').format(variavel),(variavel.isdigit()))
print('')
print(('A variavel {} contém apenas letras minúscula?').format(variavel),(variavel.islower()))
print('')
print(('A variavel {} contém apenas letras maiúsculas?').format(variavel),(variavel.isupper()))
print('')
print(('A variavel {} pode ser impressa?').format(variavel),(variavel.isprintable()))
print('')
print(('A variavel {} só tem espaço?').format(variavel),(variavel.isspace()))
print('')
print(('A variavel {} é somente um número?').format(variavel),(variavel.isnumeric()))