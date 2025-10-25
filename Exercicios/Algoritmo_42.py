# Algoritmo 42
# Entrar com um ângulo em graus e imprimir: seno, coseno, tangente, secante, co-secante e co-tangente deste ângulo

import os
os.system('cls')
import math

angulo = float(input("Digite um ângulo: "))

# Converter a entrada do tipo float para graus utilizando a classe Math
x = math.radians(angulo)

seno = math.sin(x)
coseno = math.cos(x)
tangente = math.tan(x)
secante = 1/seno
cosecante = 1/coseno
cotangente = 1/tangente

print(f"Seno: {seno}\nCoseno: {coseno}\nTangente: {tangente}\nSecante: {secante}\nCosecante: {cosecante}\nCotangente: {cotangente}")