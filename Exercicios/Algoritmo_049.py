'''Algoritmo 49
Entrar com um nome e imprimir:
todo nome:
primeiro caractere:
último caractere:
do primeiro até o terceiro:
quarto caractere:
todos menos o primeiro:
os dois últimos'''

import os 
os.system('cls')

# Todo nome
nome = input("Entre com o seu nome: ")
print(f"Todo o seu nome: {nome}")

# Primeiro caractere
print(f"Primeiro caractere do seu nome: {nome[:1]}")

# Último caractere
# Calcula o comprimento da string e subtrai 1 para que o índice imprima o último caractere
indice = len(nome)-1
print(f"Último caractere do seu nome: {nome[indice::]}")

# Do primeiro até o terceiro
print(f"Do primeiro até o terceiro caracteres do seu nome: {nome[:3]}")

# Quarto caractere
print(f"Quarto caractere do seu nome: {nome[3]}")

# Todos menos o primeiro
print(f"Todos os caracteres do seu nome, menos o primeiro: {nome[1::]}")

# Os dois últimos
indice2 = len(nome)-2
print(f"Os dois últimos caracteres do seu nome: {nome[indice2::]}")