# Algoritmo 59
# Entrar com os valores dos catetos de um triângulo retângulo e imprimir a hipotenusa

import os 
os.system('cls')
import math

# Recebendo os valores
a = int(input("Digite o valor do primeiro cateto: "))
b = int(input("Digite o valor do segundo cateto: "))

# Calculando a hipotenusa
hipotenusa = math.sqrt(((a**2) + (b**2)))
print(f"A hipotenusa é: {hipotenusa}")