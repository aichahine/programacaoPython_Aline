# Algoritmo 60
# Entrar com a razão de uma PA e o valor do 12º termo. Calcular imprimir o 10º termo da série

import os 
os.system('cls')

# Recebendo os valores
razao = int(input("Digite a razão da PA: "))
doze = int(input("Digite o décimo segundo termo da PA: "))

# razao = step
# stop = doze

# start | stop | step
# x = list(range(1, 10, 1))
# print(x)

'''
Fórmula da PA
an = a1 + (n - 1) * r

Fórmula rearranjada para descobrir o primeiro termo
a1 = an - (n - 1) * r
'''

# Calculando o primeiro termo, para calcular o décimo
a1 = doze - ((12-1)*razao)
print(f"Primeiro termo da PA: {a1}")

# Calculando o décimo termo
a10 = a1 + ((10-1)*razao)
print(f"Décimo termo da PA: {a10}")