# Algoritmo 52
# Entrar com o lado de um quadrado e imprimir:
# perimetro:
# area:
# diagonal:

import os 
os.system('cls')
import math

# Recebendo o valor do lado do quadrado
lado = int(input("Digite o valor do lado do quadrado: "))
print(f"O valor do lado do quadrado é: {lado}")

# Calculando o perímetro
perimetro = 4 * lado
print(f"O perímetro do quadrado é: {perimetro}")

# Calculando a área
area = lado * lado
print(f"A área do quadrado é: {area}")

# Calculando a diagonal
diagonal = lado * math.sqrt(2)
print(f"A diagonal do quadrado é: {diagonal}")