''' Aula 05 - Listas'''

#Adicionando itens à lista

import os
os.system('clear')

lista_compras = ["Arroz","Feijão","Açúcar","Leite"]
lista_compras.append("Batata")
print(lista_compras)

#lista_compras.append(input("Digite um produto: "))
#print(lista_compras)

lista_compras.insert(0,"Óleo")
print(lista_compras)

lista_compras.insert(3,input("Digite um produto: "))
print(lista_compras)

# Quanto uma posição é indicada e não há um valor preenchido, o retorno resulta em erro