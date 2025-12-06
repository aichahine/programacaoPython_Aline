''' Aula 06 - Listas'''
'''Crie um programa para gerenciar uma lista de compras. O programa deve:
-> Iniciar com 3 produtos
-> Adicionar 2 ovos
-> Remover um produto
-> Mostrar a lista atualizada no final
'''

import os
os.system('clear')
import time

# Iniciando a lista com 3 produtos
lista = ["arroz","feijão","café"]
print(f'Lista inicial: {lista}')
time.sleep(0.5)

# Adicionando 2 ovos
lista.append("ovos")
print(f'Nova lista de compras: {lista}')
time.sleep(0.5)

# Removendo um produto
lista.remove(lista[-1])
time.sleep(0.5)

# Mostrando a lista atualizada no final
print(f'Lista de compras atualizada: {lista}')

