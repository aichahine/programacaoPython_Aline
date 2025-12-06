# Aula do dia 29 de novembro: dicionários

# Um dicionário = banco de dados não estruturado
# começa com chave e segue com valor

'''
Exemplo de estrutura chave-valor de um dicionário:
"nome":"Senai","Nome":"Frederico"

Dentro dos dicionários é possível inserir matrizes
'''

import os
os.system('clear')

# lista usa colchetes
# dicionário usa chaves

# Sintaxe básica
dicionario = {'nome':'João'}
print(dicionario)

# Sintaxe com mais de uma chave
dicionario = {'nome':'Maria','idade':'25','gênero':'Feminino'}
print(dicionario)

# Dicionário com diferentes tipos de valor
dicionario = {'nome':'Carlos','idade':30,'altura':1.75}
print(dicionario)

# Dicionário com valores em lista
dicionario = {
    'local':'ceagesp',
    'frutas':[
        'maçã','banana','laranja'
    ]
}
print(dicionario)

dicionario = {
    "id":55,
    "País":"Brasil",
    "Região":"América do Sul",
    "População":201032714,
    "PrincipaisCidades":[
        {
            "NomeCidade":"São Paulo",
            "População":1182876,
        },
        {
            "NomeCidade":"Rio de Janeiro",
            "População":6323037,
        }
    ]
}
print(dicionario)