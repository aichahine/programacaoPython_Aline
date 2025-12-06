import os
os.system('clear')
# Usando o valor da variável fora da função

def somar(a,b,c):
    total=a+b+b
    return total

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))

total = somar(nota01,nota02,nota03)
media = total/3
print(media)
print(total)