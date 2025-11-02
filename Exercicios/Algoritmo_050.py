'''Algoritmo 50
Entrar com a base e a altura de um retângulo e imprimir a seguinte saída:
perímetro
area
diagonal'''

import os 
os.system('cls')
import math

x = float(input("Digite o valor da base do retângulo: "))
y = float(input("Digite o valor da altura do retângulo: "))

perimetro = 2 * (x + y)
area = x * y
diagonal = math.sqrt(x*x + y*y)

print(f"Perímetro: {perimetro}\nÁrea: {area}\nDiagonal: {diagonal}")