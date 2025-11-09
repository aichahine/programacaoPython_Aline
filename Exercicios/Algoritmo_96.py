# Algoritmo 96
# Entrar com um número e informar se ele é divisível por 3 e por 7.

import os
os.system('cls')

numero=int(input("Digite um número: "))

if(numero%3==0 and numero%7==0):
  print(f"O número {numero} é divisível por 3 e por 7.")
else:
  print(f"O número {numero} não é divisível por 3 e por 7.")