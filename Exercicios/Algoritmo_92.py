# algoritmo 92
# Construir um algoritmo que leia dois números e efetue a adição.
# Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8;
# caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.

import os
os.system('clear')

primeiroNumero=int(input("Digite o primeiro número: "))
segundoNumero=int(input("Digite o segundo número: "))

soma = primeiroNumero + segundoNumero

if(soma>20):
    soma=soma+8
    print(f"O resultado é maior que 20: {soma}.")
else:
    menor = soma - 5
    print(f"O resultado é menor ou igual que 20: {menor}.")
