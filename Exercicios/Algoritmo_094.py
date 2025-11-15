# algoritmo 94
# Entrar com um número e imprimir uma das mensagens: é múltiplo de 3 ou não
# é múltiplo de 3.

import os
os.system('clear')

num1=int(input("Digite um número: "))

if(num1%3==0):
    print(f'É um número múltiplo de três: {num1},')
else:
    print(f"Não é um número múltiplo de três: {num1}.")