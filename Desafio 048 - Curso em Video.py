# Faça um programa que calcule a soma entre todos os números ímpares que são
# múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0

for impar in range(1, 501, 2):
    if impar%3 == 0:
        soma += impar
print(soma)