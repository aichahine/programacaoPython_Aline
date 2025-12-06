import os
os.system('clear')
'''Funções
. Funções são trechos repetitivos que são usados conforme for necessário

Função (menos utilizado)
. Sem retorno
. Sem parâmetro

Função
. Sem retorno
. Com parâmetro

Função
. Com retorno
. Com parâmetro
'''

# Criação da função sem parâmetro e sem retorno
def somar():
    num_01 = int(input("Digite um número: "))
    num_02 = int(input("Digite um número: "))
    totalSoma = num_01+num_02
    print(f"Total da soma: {totalSoma}")

def subtrair():
    num_01 = int(input("Digite um número: "))
    num_02 = int(input("Digite um número: "))
    totalsub = num_01-num_02
    print(f"Total da subtração: {totalsub}")

def multiplicar():
    num_01 = int(input("Digite um número: "))
    num_02 = int(input("Digite um número: "))
    totalMulti = num_01*num_02
    print(f"Total da multiplicação: {totalMulti}")

def dividir():
    num_01 = int(input("Digite um número: "))
    num_02 = int(input("Digite um número: "))
    totaldiv = num_01/num_02
    print(f"Total da divisão: {totaldiv}")

def solicitarOperacao():
    op = input("Digite a operação: ")
    if(op=="+"):
        somar()
    elif(op=="-"):
        subtrair()
    elif(op=="*"):
        multiplicar()
    elif(op=="/"):
        dividir
    else:
        print("Ai que burro, dá zero pra ele!")

solicitarOperacao()