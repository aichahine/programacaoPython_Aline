# Algoritmo 58
# Entrar com valores para xnum 1, xnum2 e xnum3 e imprimir o valor de x
# x = xnum1 + xnum2 / (xnum3 + xnum1) + 2 ( xnum1 - xnum2 ) + log₂64

import os 
os.system('cls')
import math

# Recebendo os valores
xnum1 = int(input("Digite o valor do primeiro número: "))
xnum2 = int(input("Digite o valor do segundo número: "))
xnum3 = int(input("Digite o valor do terceiro número: "))

# Calculando o valor de x
# Logaritmo: log(número,base)
x = xnum1 + (xnum2/(xnum3+xnum1)) + (2*(xnum1-xnum2)) + (math.log(64,2))

# Imprimindo o resultado
print(f"O valor de x é: {x}")