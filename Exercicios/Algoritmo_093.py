# algoritmo 93
# Entrar com um número e imprimir a raiz quadrada do número caso ele seja
# positivo e o quadrado do número caso ele seja negativo.

import os
os.system('clear')
import math

num1=int(input("Digite um número: "))

if(num1>=0):
    raiz=math.sqrt(num1)
else:
    quadrado = math.pow(num1,2)
    print(f'A raiz é: {quadrado}.')