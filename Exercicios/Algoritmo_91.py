# algoritmo 91
# Construir um algoritmo que leia dois valores numéricos inteiros e efetue a
# adição; caso o resultado seja maior que 10, apresentá-lo.

import os
os.system('clear')

primeiroNumero=int(input("Digite o primeiro número: "))
segundoNumero=int(input("Digite o segundo número: "))

soma = primeiroNumero + segundoNumero
if(soma>10):
    print(f"O resultado é: {soma}.")