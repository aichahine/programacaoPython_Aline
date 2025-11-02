# Aula de 01 de novembro de 2025

import os
os.system('clear')

# A modelo deve ter 16 anos e 1.70 de altura

idade = int(input("Digite a idade da candidata: "))
altura = float(input("Digite a altura da candidata: "))
etnia = input("Digite a etnia da candidata: ")

idade_certa = idade == 16
altura_certa = altura == 1.70

if(idade_certa and altura_certa):
    print("Aprovada")
else:
    print("Reprovada")