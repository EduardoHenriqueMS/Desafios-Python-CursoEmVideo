# Crie um script Python que leia o dia, o mes e o ano de nascimento de
# pessoa e mostre uma mensagem com a data informada

nome = input('Informe o seu nome: ')
sobrenome = input('Informe o seu sobrenome: ')

print('Bem-vindo',nome,sobrenome + '!')

dia = input('Informe o dia do seu nascimento em números: ')
mes = input('Informe o mes do seu nascimento em números: ')
ano = input('Informe o ano do seu nascimento em números: ')

print('O usuário:',nome,sobrenome)
print('Nasceu na data:',dia,'/',mes,'/',ano)

correto = input('Correto? ')