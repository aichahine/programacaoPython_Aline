# algoritmo 106
# Entrar com um nome e imprimi-lo se o primeiro caractere for a letra A (considerar letra minúscula ou maiúscula)

import os
os.system('cls')

nome = input("Digite um nome: ")

nome = nome.lower()

if(nome[:1] == 'a'):
    print(f"O nome é {nome}")
else:
    print(f"O nome é: {nome}.\nA primeira letra deste nome não é a letra A")