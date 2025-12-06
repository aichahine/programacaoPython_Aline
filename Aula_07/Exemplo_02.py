# Aula do dia 08 de novembro
# Laço while

import os
os.system('clear')
import time

soma = 0
cont = 0

nota = float(input("Digite a nota: "))

while (nota>0):
    soma = soma+nota
    cont+=1
    nota = float(input("Digite a nota: "))

media = soma/cont

print(f'A média é: {media}.')