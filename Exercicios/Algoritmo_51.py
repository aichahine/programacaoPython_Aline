'''Algoritmo 51
Entrar com o raio de um circulo e imprimir a seguinte saída:
perimetro
area'''

import os 
os.system('cls')
import math

r = float(input("Digite o raio de um círculo: "))
perimetro = 2 * math.pi * r
#area = math.pi*(r*math.pow)

print(f"Perímetro: {perimetro}")