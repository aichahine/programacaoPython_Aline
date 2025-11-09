# Aula do dia 08 de novembro
# Laço while

import os
os.system('clear')

cont = 0
acm = 0

numero = int(input("Digite um número ou 0 para encerrar: "))

while (numero != 0):
    acm = acm + numero
    numero = int(input("Digite um número ou 0 para encerrar: "))
print(f'Programa encerrado e a soma total foi: {acm}')