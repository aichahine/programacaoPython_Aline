# Aula de 25 de outubro de 2025

import os
os.system('cls')

nome = "Senai"
print(nome[::2])

# Função para formatar o texto em minúsculas
texto = "Senai"
print(f"Texto em minúsculas: {texto.lower()}")

# Função para formatar o texto em maiúsculas
texto = "Senai"
print(f"Texto em maiúsculas: {texto.upper()}")

# Função para substituir texto
textoAlterado = texto.replace("Jacó", "Jacob")
print(f"Texto alterado: {textoAlterado}")

# Função para inverter a ordem (apenas para string)
texto = texto[::-1]
print(f"Texto invertido: {texto}")

numero = "123456"
numeroInvertido = numero[::-1]
print(f"Número invertido: {numeroInvertido}")