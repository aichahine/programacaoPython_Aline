# Algoritmo 105
# Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens:
# carioca
# paulista
# mineiro
# outros estados

import os
os.system('cls')

sigla = input("Digite a sigla do Estado: ")

# Formata a string em minúsculas
sigla = sigla.lower() 

if(sigla == 'rj'):
    print("Carioca")
elif(sigla == 'sp'):
    print("Paulista")
elif(sigla == 'mg'):
    print("Mineiro")
else:
    print("Outros estados")