# Algoritmo 99
# Ler um número inteiro de 3 casas decimais e imprimir se o algarismo da casa
# das centenas é par ou ímpar.

import os
os.system('cls')

numero = int(input("Digite um número inteiro com três dígitos: "))
centena = numero/100

if(numero[:1]%2==0):
    print(f"O algarismo da casa das centenas é par: {centena}")
else:
    print(f'O algaristmo da casa das centenas é ímpar: {centena}')

# inacabado

'''
Parte inteira da divisão (//)
Esse é o complemento do operador módulo, pois aqui obtemos a parte inteira da divisão, em vez do resto. Então, na divisão de 10 por 3, o resultado seria 3.

Esse operador é bem interessante para alguns cálculos, e você já pode tê-lo visto, por exemplo, em conversões de hora.

num1 = 10
num2 = 3

print("Parte inteira da divisão:")
print(num1//num2)
Parte inteira da divisão (//)
Exemplo prático
Podemos utilizar os operadores aritméticos para realizar cálculos dentro do nosso código, como calcular o lucro de uma empresa.

faturamento = 400
custo = 150

lucro = faturamento - custo

print("O lucro foi de:")
print(lucro)
Calculando lucro com Python
'''