# Algoritmo 41
# Entrar com quatro números e imprimir a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4

import os 
os.system('cls')

numero01 = int(input("Digite o primeiro número: "))
numero02 = int(input("Digite o segundo número: "))
numero03 = int(input("Digite o terceiro número: "))
numero04 = int(input("Digite o quarto número: "))

mediaP = ((numero01*1) + (numero02*2) + (numero03*3) + (numero04*4)) / 4

print(f"Média ponderada: {mediaP}")

