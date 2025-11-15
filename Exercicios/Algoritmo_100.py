# Algoritmo 100
# Ler um número inteiro de 4 casas e imprimir se é ou não múltiplo de quatro o
# número formado pelos algarismos que estão nas casas das unidades de milhar
# e das centenas.

import os
os.system('cls')

numero = int(input("Digite um número inteiro com quatro dígitos: "))
milhar = numero//1000
centena = numero//100

if(milhar%4==0 and centena%4==0):
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


# Ler um número inteiro de 4 dígitos
numero = int(input("Digite um número inteiro de 4 dígitos: "))

# Verificar se o número tem 4 dígitos
if 1000 <= numero <= 9999:
    # Extrair os dígitos das casas das unidades de milhar e das centenas
    milhar = numero // 1000  # Casa das unidades de milhar
    centena = (numero // 100) % 10  # Casa das centenas
    
    # Formar o novo número
    novo_numero = milhar * 10 + centena

    # Verificar se o novo número é múltiplo de 4
    if novo_numero % 4 == 0:
        print(f"O número {novo_numero} é múltiplo de 4.")
    else:
        print(f"O número {novo_numero} não é múltiplo de 4.")
else:
    print("Por favor, digite um número válido de 4 dígitos.")