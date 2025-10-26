# Algoritmo 55
# Criar um algoritmo que calcule e imprima a área de um losango.

import os 
os.system('cls')

# Recebendo as dimensões do losango
diagonal1 = int(input("Digite o valor da primeira diagonal: "))
diagonal2 = int(input("Digite o valor da segunda diagonal: "))

# Calculando a área
area = (diagonal1 * diagonal2) / 2
print(f"A área do losango é: {area}")