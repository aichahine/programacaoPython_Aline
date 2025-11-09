# algoritmo 262
# Entrar com números e imprimir o triplo de cada número
# o algoritmo acaba quando entrar o número -999

import os
os.system('clear')

numero = int(input("Digite um número ou -999 para encerrar: "))

contador = 0

while (numero != -999):
    triplo = numero*3
    numero = int(input("Digite mais um número ou -999 para encerrar: "))
print(f"Programa encerrado. O triplo do último número digitado é: {triplo}")

# inacabado