import os
os.system('clear')
'''
01 - Crie um dicionário chamado pessoa com as chaves "nome", "idade" e "cidade",
e atributa valores a elas. Em seguida, imprima o valor da chave "nome",

02 - Crie uma tupla chamada cores com os valores "vermelho", "verde", e "azul".
Acesse e imprima o segundo elemento da tupla.

03 - Dado o dicionário estoque abaixo, atualize o valor da chave "maçãs"
para 30 e adicione uma nova chave "uvas" com valor 50. Imprima o dicionário atualizado.
'''

'''Exercicio 01'''
pessoa = {
    "nome":"Aline",
    "idade":39,
    "cidade":"São Paulo",
    }
print(pessoa["nome"])

'''Exercicio 02'''
cores = ("vermelho","verde","azul")
print(cores[1])

'''Exercicio 3'''
estoque = {"maçãs":30,"uvas":50}
print(estoque)