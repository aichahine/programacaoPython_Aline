import os
os.system('clear')

# Sintaxe com mais de uma chave

dicionario = {
    "nome":"Maria",
    "idade":25,
    "gênero":"Feminino"
}

print(dicionario["nome"])

# Sintaxe com outro dicionário como valor

dicionario = {
    "pessoa":{
        "nome":"Pedro",
        "idade":35
    }
}

# Acessando o nome dentro do dicionário pessoa
print(dicionario["pessoa"]["nome"])