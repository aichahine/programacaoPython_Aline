# Algoritmo 107
# Entrar com o nome de uma pessoa e só imprimi-lo se o prenome for JOSÉ

import os
os.system('clear')

nomeCompleto = input("Digite o nome completo: ")
lista = nomeCompleto.split()
primeiroNome = lista[:1]
prenome = lista[1]
ultimoNome = lista[-1]
#print(f'Nome completo: {nomeCompleto}\nPrimeiro nome: {primeiroNome}\nPrenome: {prenome}\nÚltimo nome: {ultimoNome}')

if(prenome == 'JOSÉ'):
    print(f"O prenome é {prenome}")
else:
    print(f"O prenome não é JOSÉ, o prenome é: {prenome}.")