# algoritmo 65
# Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula: volume = 3.14159 * R2 * altura

import os 
os.system('cls')
import math

# Fórmula do volume
# volume = pi * raio ao quadrado * altura

# Recebendo os valores
diametro = float(input("Digite o valor do diâmetro da lata: "))
raio = diametro / 2

altura = float(input("Digite o valor da altura da lata: "))

# Calculando o volume
volume = math.pi * (raio**2) * altura

print(f"O volume da lata é: {volume}")