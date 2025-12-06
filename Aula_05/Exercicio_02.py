'''Crie um sistema simples de estoque que
-> Verifica se o produto está disponível
-> Mostra o primeiro e o último produto da lista
-> Adiciona 5 produtos usando o for
-> Verifica a lista e adiciona separado um último item'''
import os
os.system('clear')

estoque = ["lápis","borracha","caneta","apontador"]

busca = input("Digite um produto: ")
busca = busca.lower()

# Verificando se o produto está disponível
if(busca in estoque):
    print(f"Sim, o produto: {busca} está disponível")
else:
    print(f"Não, o produto: {busca} não está disponível")

# Mostrando o primeiro e o último produtos da lista
primeiro = estoque[0]
ultimo = estoque[-1]
print(f"O primeiro produto da lista é: {primeiro}\nO último produto da lista é: {ultimo}")

# Adicionando 5 produtos utilizando o for
cont = 0
for i in range(5):
    estoque.append(input("Digite um novo produto: "))
    cont+=1
print(f"Estoque com os cinco novos produtos: {estoque}")

# Verificando a lista e adiciona separado um último item (adicionar um novo item ao fim da lista)
