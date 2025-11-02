# Aula de 01 de novembro de 2025

import os
os.system('clear')

nota_01 = float(input("Digite a nota 1: "))
nota_02 = float(input("Digite a nota 2: "))
nota_03 = float(input("Digite a nota 3: "))
nota_04 = float(input("Digite a nota 4: "))

media = (nota_01+nota_02+nota_03+nota_04)/4

print(f"A média é: {media}")

if(media >= 7):
    print("Aprovado!!")
else:
    print("Reprovado!!")