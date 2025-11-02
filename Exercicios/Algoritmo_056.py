# Algoritmo 56
# Entrar com nome e idade. Imprimir a seguinte saída:
# nome:
# idade:

import os 
os.system('cls')

# Recebendo o nome e a idade
# Partindo do pressuposto que a entrada seja primeiro nome e idade numérica: Aline 39
informacoes = input("Digite o nome e a idade: ")
print(F"Nome e idade digitados: {informacoes}")

# Comprimento da string, removendo a idade
indice = len(informacoes)-2

# Nome
# Percorre a lista da esquerda para a direita, até a posição imediatamente anterior
print(f"Nome: {informacoes[:indice]}")

# Idade - os dois últimos caracteres
# Percorre a lista da direita para a esquerda e imprime incluindo a posição indicada
print(f"Idade: {informacoes[-2:]}")