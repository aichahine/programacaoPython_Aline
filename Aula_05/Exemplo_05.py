''' Aula 05 - Listas'''

#Removendo itens à lista

import os
os.system('clear')
import time

lista_compras = ["Arroz","Feijão","Açúcar","Leite", "Batata"]
print(f'Lista de compras: {lista_compras}')

# Removendo pelo item
lista_compras.remove("Batata")
print(f'Lista de compras, removendo pelo nome: {lista_compras}')


lista_compras = ["Arroz","Feijão","Açúcar","Leite", "Batata"]
print(f'Lista de compras: {lista_compras}')

# Removendo pela posição
lista_compras.remove(lista_compras[-1])
print(f'Lista de compras, removendo pela posição: {lista_compras}')

# Listando as posições e os itens da lista
cont = 0
for lista in lista_compras:
    print(f"Posição: {cont} ||  Item: {lista}")
    time.sleep(0.5)
    cont+=1