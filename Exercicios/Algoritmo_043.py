# Algoritmo 43
# Entrar com um número e imprimir o logaritmo desse número na base 10

import os
os.system('cls')
import math

x = float(input("Entre com um número: "))
logaritmo = math.log10(x)

print(f"Logaritmo de {x} na base 10: {logaritmo}")