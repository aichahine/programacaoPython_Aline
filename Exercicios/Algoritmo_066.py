''' Algoritmo 66
Efetuar o cálculo da quantidade de litros de combustível gastos em uma viagem, 
sabendo-se que o carro faz 12 km com um litro. Deverão ser fornecidos o tempo 
gasto na viagem e a velocidade média.
Utilizar as seguintes fórmulas:
. distância = tempo x velocidade.
. litros usados = distância / 12.
O algoritmo deverá apresentar os valores da velocidade média, tempo gasto
na viagem, distância percorrida e a quantidade de litros utilizados na viagem.'''

import os 
os.system('cls')
import math

'''
1L = 12km
tempo
velocidade
'''

# Recebendo os valores
tempo = float(input("Digite quantas horas foram gastas na viagem: "))
velocidade = float(input("Digite a velocidade média (km/h) durante a viagem: "))

# Calculando a distância
distancia = tempo * velocidade

# Calculando o consumo
litros = distancia / 12

print(f"\nA velocidade média foi: {velocidade} km/h.")
print(f"O tempo gasto na viagem foi: {tempo} h.")
print(f"A distância percorrida foi de: {distancia} quilômetros.")
print(f"A quantidade de litros utilizandos na viagem foi: {litros}L.")