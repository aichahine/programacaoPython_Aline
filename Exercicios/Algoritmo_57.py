# Algoritmo 57
# Entrar com as notas da PR 1 e PR2 e imprimir a média final:
# m truncada:
# arredondada:

import os 
os.system('cls')
import math

# Recebendo as notas
pr1 = float(input("Digite a primeira nota: "))
pr2 = float(input("Digite a segunda nota: "))

# Calculando a média
media = (pr1 + pr2)/2
print(f"A média final é: {media}")

# Calculando a média final truncada
truncada = math.trunc(media)
print(f"A média truncada é: {truncada}")

# Calculando a média final arredondada

# Arredondamento para cima
arredondadaC = math.ceil(media)
print(f"A média arredondada para cima é: {arredondadaC}")

# Arredondamento para baixo
arredondadaB = math.floor(media)
print(f"A média arredondada para baixo é: {arredondadaB}")