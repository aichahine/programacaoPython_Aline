# algoritmo 95
# Entrar com um número e informar se ele é ou não divisível por 5.

import os
os.system('clear')

num1=int(input("Digite um número: "))

if(num1%5==0):
    print(f'É um número divisível por cinco: {num1}.')
else:
    print(f"Não é um número divisível por cinco: {num1}.")