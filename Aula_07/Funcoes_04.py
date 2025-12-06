import os
os.system('clear')
# Criação da função com parâmetro e sem retorno
def somar(a,b):
    totalSoma = a+b
    print(f"Total da soma: {totalSoma}")

def subtrair(a,b):
    totalSub = a-b
    print(f"Total da subtração: {totalSub}")

def multiplicar(a,b):
    totalMulti = a*b
    print(f"Total da multiplicação: {totalMulti}")

def dividir(a,b):
    totalDiv = a/b
    print(f"Total da divisão: {totalDiv}")

def solicitarOperacao(a,b):
    op = input("Digite a operação: ")
    if(op=="+"):
        somar(a,b)
    elif(op=="-"):
        subtrair(a,b)
    elif(op=="*"):
        multiplicar(a,b)
    elif(op=="/"):
        dividir(a,b)
    else:
        ("Ai que burro, dá zero pra ele!")

num_01 = int(input("Digite um número: "))
num_02 = int(input("Digite um número: "))

solicitarOperacao(num_01,num_02)