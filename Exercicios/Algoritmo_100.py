# Algoritmo 100
# Ler um número inteiro de 4 casas e imprimir se é ou não múltiplo de quatro o
# número formado pelos algarismos que estão nas casas das unidades de milhar
# e das centenas.

import os
os.system('cls')

numero = int(input("Digite um número inteiro com quatro dígitos: "))
milhar = numero//1000
''' Centena: Para obter o dígito da centena, dividimos o número por 100
    para mover o dígito da centena para a posição mais à esquerda e, em seguida,
    usamos o operador de módulo (%) com 10 para obter apenas o último dígito resultante.
    No código, isso é feito assim:'''
centena = (numero // 100) % 10  # Casa das centenas

# Formar o novo número
novoNumero = milhar * 10 + centena
print(f'O novo número formado é: {novoNumero}')

if(novoNumero%4==0):
    print(f"O algarismo do milhar e da centena são múltiplos de quatro, os algarismos são:\nMilhar: {milhar}\nCentena: {centena}")
else:
    print(f'Não são múltiplos de quatro:\nMilhar: {milhar}\nCentena: {centena}')

# Parte inteira da divisão (//)
# Esse é o complemento do operador módulo, pois aqui obtemos a parte inteira da divisão, em vez do resto.
# Então, na divisão de 10 por 3, o resultado seria 3.

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# parteInteira = num1 // num2
# print(f"Parte inteira da divisão: {parteInteira}")