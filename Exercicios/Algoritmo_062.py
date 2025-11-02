''' Algoritmo 62
Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo 
desconto. Faça um algoritmo que possa entrar com o valor de um produto e imprima o novo valor 
tendo em vista que o desconto foi de 9%'''

import os 
os.system('cls')

# Recebendo o valor
valorProd = int(input("Digite o valor de um produto: "))

# Calculando o novo valor
novoValor = valorProd - (valorProd * 0.09)

print(f"O novo valor do produto é:{novoValor}")