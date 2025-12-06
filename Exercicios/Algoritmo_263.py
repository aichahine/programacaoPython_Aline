# Algoritmo 263
# Entrar com números enquanto forem positivos e imprimir quantos números
# foram digitados.

import os
os.system('clear')

numero = int(input("Digite um número: "))

contador = 0

while (numero > 0):
    numero = int(input("Digite mais um número ou um número negativo para encerrar: "))
print(f"Programa encerrado.\nO último número digitado é: {numero}.")