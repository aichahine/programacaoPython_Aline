# Algoritmo 34
# Ler um número inteiro e imprimir seu sucessor e seu antecessor

import os 
os.system('cls')

numero = int(input("Digite um número: "))

sucessor = numero + 1
antecessor = numero - 1

print(f"Antecessor: {antecessor}, número: {numero}, sucessor: {sucessor}")