# Algoritmo 40
# Entrar com dois números inteiros e imprimir a seguinte saída:
# dividendo
# divisor
# resto
# quociente

import os 
os.system('cls')

dividendo = float(input("Digite o primeiro número: "))
divisor = float(input("Digite o segundo número: "))

quociente = dividendo / divisor
resto = dividendo%divisor

print(f"Dividendo: {dividendo} | divisor: {divisor}\nResto: {resto} | quociente: {quociente}")