import os
os.system('clear')
# Criação da função com parâmetro e com retorno

def somar(a,b,c):
    total=a+b+b
    return total

def mediaTresValores(a,b,c):
    media = somar(a,b,c)/3
    print(media)

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))

mediaTresValores(nota01,nota02,nota03)