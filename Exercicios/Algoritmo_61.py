# Algoritmo 61
# Entrar com a razão de uma PG e o valor do 12º termo. Calcular e imprimir o 5º termo da série

import os 
os.system('cls')
import math

# Recebendo os valores
razao = int(input("Digite a razão da PG: "))
doze = int(input("Digite o décimo segundo termo da PG: "))

'''
Fórmula da PG
an = a1 * q^(n-1)
an = número que queremos saber
a1 = primeiro número
q^(n-1) = razão elevada ao número que queremos obter, menos 1

Fórmula rearranjada para descobrir o primeiro termo
a1 = an / (q^(n-1))
'''

# Calculando o primeiro termo, para calcular o quinto
a1 = doze / (razao**(12-1))
print(f"Primeiro termo da PG: {a1}")

# Calculando o quinto termo
a5 = a1 * (razao**(5-1))
truncado = math.trunc(a5)
print(f"Quinto termo da PG: {truncado}")