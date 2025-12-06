import os
os.system('clear')
import time

# Criando um dicionário com compreensão de dicionário

# Dicionario com o quadrado de 1 a 5
# x elevado ao quadro, laço for 
dicionario = {x: x**2 for x in range(1, 6)}
time.sleep(0.6)
print(dicionario)