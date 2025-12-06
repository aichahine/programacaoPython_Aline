# Algoritmo 265
# Ler vários números e informar quantos números entre 100 e 200 foram
# digitados. Quando o valor 0 (zero) for lido, o algoritmo deverá cessar sua
# execução.

import os
os.system('clear')

cont = 0

numero = int(input("Digite um número qualquer, ou o número 0 para encerrar: "))

while (numero != 0):

    if(numero>=100 and numero<=200):
        cont+=1
        numero = int(input("Digite mais um número ou o número 0 para encerrar: "))
    elif(numero<100 or numero>100):
        break
print(f'Programa encerrado.\nNúmeros entre 100 e 200: {cont}')