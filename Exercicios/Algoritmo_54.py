# Algoritmo 53
# Criar um algoritmo que calcule e imprima a área de um triângulo

import os 
os.system('cls')

base = int(input("Digite o valor da base do triângulo: "))
altura = int(input("Digite o valor do lado do triângulo: "))

area = (base * altura) / 2
print(f"Área: {area}")