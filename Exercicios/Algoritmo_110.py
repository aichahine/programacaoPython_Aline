# Algoritmo 110
# Criar um algoritmo que leia dois números e imprimir uma mensagem dizendo
# se são iguais ou diferentes.

import os
os.system('clear')

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo: "))

if(primeiroNumero == segundoNumero):
    print("Os números são iguais")
else:
    print("Os números são diferentes")