# Algoritmo 42
# Entrar com um ângulo em graus e imprimir: seno, coseno, tangente, secante, co-secante e co-tangente deste ângulo

import os
os.system('cls')
import math

x = float(input("Digite um ângulo: "))

seno = math.sin(x)
coseno = math.cos(x)
tangente = math.tan(x)
# secante = math.asin(x)
# cosecante = math.acos(x)
cotangente = math.atan(x)

# print(f"Seno: {seno}\nCoseno: {coseno}\nTangente: {tangente}\nSecante: {secante}\nCosecante: {cosecante}\nCotangente: {cotangente}")
print(f"Seno: {seno}\nCoseno: {coseno}\nTangente: {tangente}\nCotangente: {cotangente}")