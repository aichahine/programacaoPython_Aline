# Algoritmo 101
# Construir um algoritmo que indique se o número digitado está compreendido entre 20 e 90 ou não

import os
os.system('clear')

numero = int(input("Digite um número: "))

if(numero>=20 and numero<=90):
    print(f"O número {numero} ESTÁ entre 20 e 90")
else:
    print(f"O número {numero} NÃO ESTÁ entre 20 e 90")