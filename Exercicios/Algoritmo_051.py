'''Algoritmo 51
Entrar com o raio de um circulo e imprimir a seguinte saída:
perimetro
area'''

import os 
os.system('cls')
import math

r = int(input("Digite o raio de um círculo: "))

perimetro = 2 * math.pi * r
print(f"Perímetro: {perimetro}")

area = math.pi * (r ** 2)
print(f"Área: {area}")