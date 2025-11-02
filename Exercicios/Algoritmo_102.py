# Algoritmo 102
# Entrar com um número e imprimir uma das mensagens: maior do que 20, igual a 20 ou menor do que 20

import os
os.system('clear')

numero = int(input("Digite um número: "))

if(numero>20):
    print("Maior do que 20")
elif(numero==20):
    print("Adolescente")
elif(numero<20):
    print("Menor que 20")
else:
    print("Erro")