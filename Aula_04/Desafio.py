# Aula do dia 08 de novembro
# Tabuada

import os
os.system('clear')
import time

cont = 1
numero = int(input("Digite o número da tabuada: "))

while (cont <=10):
    tabuada = numero*cont
    print(f"{numero} x {cont} = {tabuada}")
    time.sleep(0.6)
    cont+=1