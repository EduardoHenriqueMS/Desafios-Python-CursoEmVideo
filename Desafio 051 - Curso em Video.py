# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Digite um número inteiro qualquer: "))
razao = int(input("Digite a razão dessa Progressão Aritmética: "))

print("------"*10)
print("Os dez primeiros termos dessa PA, são:")
print(f"{primeiro}")

for i in range(1, 10):
    primeiro += razao
    print(f"{primeiro}")