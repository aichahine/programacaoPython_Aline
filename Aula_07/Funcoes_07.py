import os
os.system('clear')

'''Exercício 1 - Função que retorna o maior número
Crie uma função chamada maior(a,b) que receba dois números e retorne o maior deles

Exercício 2 - Função que retorna uma string invertida
Crie uma função inverter(texto) que retorne a string invertida'''

'''Exercício 1'''

def maior(a,b):
    if(a>b):
        print(f"O primeiro número: {a} é maior do que o segundo número: {b}")
    elif(a==b):
        print(f"Os números são iguais")
    elif(b>a):
        print(f"O segundo número: {b} é maior que o primeiro número: {a}")
    else:
        print:(f"Comando inválido")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

maior(num1,num2)