# Aula do dia 08 de novembro
# Laço while

import os
os.system('clear')
import time

cont = 0
acm = 0

while (True):
    numero = int(input("Digite um número ou 0 para encerrar: "))
    acm = acm + numero
    
    if(numero==0):
        break
        time.sleep(0.6)

print(f'Programa encerrado e a soma total foi: {acm}')