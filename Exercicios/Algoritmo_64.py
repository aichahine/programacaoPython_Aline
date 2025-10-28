''' Algoritmo 64
Ler uma temperatura em graus Celsius e apresentá-la convertida
 em Fahrenheit. A fórmula de conversão é:
F = (9C + 160) / 5 
F é a temperatura em Fahrenheit e
C é a temperatura em graus Celsius
'''

import os 
os.system('cls')

# Recebendo os valores
celsius = float(input("Digite a temperatura em Celsius: "))

# Convertendo
fahrenheit = ((9*celsius)+160) / 5

print(f"A temperatura em Fahrenheit é: {fahrenheit}")