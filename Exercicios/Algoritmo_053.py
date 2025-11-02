# Algoritmo 52
# Entrar com os lados a, b, c de um paralelepípedo. Calcular e imprimir a diagonal

import os 
os.system('cls')
import math

a = int(input("Digite o valor do lado A do paralelepípedo: "))
b = int(input("Digite o valor do lado B do paralelepípedo: "))
c = int(input("Digite o valor do lado C do paralelepípedo: "))

diagonal = math.sqrt(a**2 + b**2 + c**2)
print(f"Diagonal: {diagonal}")