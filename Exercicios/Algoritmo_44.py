# Algoritmo 44
# Entrar com o número e a base em que se deseja calcular o logaritmo desse número e imprimi-lo

import os
os.system('cls')
import math

x = float(input("Entre com um número: "))
base = float(input("Entre com a base: "))

logaritmo = math.log(x,base)

print(f"Logaritmo de {x} na base {base}: {logaritmo}")