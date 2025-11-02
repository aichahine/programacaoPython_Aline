# Algoritmo 47
# Entrar com um número no formato CDU e imprimir invertido: UDC. (Exemplo: 123, sairá 321.) O número deverá ser armazenado em outra variável antes de ser impresso

import os 
os.system('cls')

# Solicito o input como número mas não declaro o tipo int
# para que seja possível aplicar a ordenação de string
numero = input("Digite o número com três dígitos: ")
numeroInvertido = numero[::-1]
print(f"Número invertido: {numeroInvertido}")