# Algoritmo 99
# Ler um número inteiro de 3 casas decimais e imprimir se o algarismo da casa
# das centenas é par ou ímpar.

import os
os.system('cls')

numero = int(input("Digite um número inteiro com três dígitos: "))
centena = numero//100

if(centena%2==0):
    print(f"O algarismo da casa das centenas é par: {centena}")
else:
    print(f'O algaristmo da casa das centenas é ímpar: {centena}')

# Parte inteira da divisão (//)
# Esse é o complemento do operador módulo, pois aqui obtemos a parte inteira da divisão, em vez do resto.
# Então, na divisão de 10 por 3, o resultado seria 3.

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# parteInteira = num1 // num2

# print(f"Parte inteira da divisão: {parteInteira}")