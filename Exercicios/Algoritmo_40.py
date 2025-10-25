# Algoritmo 40
# Entrar com dois números inteiros e imprimir a seguinte saída:
# dividendo
# divisor
# resto
# quociente

import os 
os.system('cls')

numero01 = int(input("Digite o primeiro número: "))
numero02 = int(input("Digite o segundo número: "))

divisao = numero01 / numero02

# ????????
print(f"Dividendo: {numero01} | divisor: {numero02}\nResto: {divisao} | quociente: {divisao}")