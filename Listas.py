import os
os.system('cls')

vendas = [100, 50, 14, 20, 30, 700]

'''Soma dos elementos
totalVendas = sum(vendas)
print(f"Vendas: {totalVendas}")'''

'''Tamanho da lista
qtdeVendas = len(vendas)
print(f"Quantidade de vendas: {qtdeVendas}")'''

'''Valor máximo da lista
print(max(vendas))'''

'''Valor mínimo da lista
print(min(vendas))'''

'''Selecionar o elemento da lista pelo índice / posição
print(vendas[5])'''

listaProdutos = ["iphone", "airpod", "ipad", "macbook"]

'''Retorna verdadeiro ou falso se a string existir na lista
produtoProcurado = input("Pesquise pelo nome do produto: ")
produtoProcurado = produtoProcurado.lower()
print("apple watch" in listaProdutos)'''

'''MÉTODOS DE EDIÇÃO DE LISTA
Adicionar um item na lista
listaProdutos.append("apple watch")
print(listaProdutos)

Remover um item na lista
listaProdutos.remove("apple watch")
print(listaProdutos)

Remover um item da lista de acordo com o índice
listaProdutos.pop(0)
print(listaProdutos)

precos = [1000, 1500, 3500]
Editar um item na lista
Para editar o item de uma lista: indicar o índice e atribuir a edição / modificação
precos[0] = 6000
print(precos)'''

novaLista = ["iphone", "airpod", "ipad", "macbook", "iphone", "ipad", "iphone"]
'''Contar quantas vezes um item aparece na lista
print(novaLista.count("iphone"))'''

'''# Ordenar uma lista
# Por padrão, ordena ordem alfabética / crescente
novaLista.sort(reverse)
print(novaLista)'''

# Para ordenar em ordem reversa / decrescente
novaLista.sort(reverse=True)
print(novaLista)