''' Aula 06 - Listas'''

import os
os.system('clear')

# Procurando itens

lista_compras = ["arroz","feijão","açúcar","leite", "batata"]

produto_procurado = input("Digite um produto: ")
produto_procurado = produto_procurado.lower()

if(produto_procurado in lista_compras):
    print(f"{produto_procurado} está disponível")
else:
    print(f"{produto_procurado} não está disponível")