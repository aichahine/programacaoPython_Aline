# Algoritmo 67
# Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:
# prestação = valor + (valor*(taxa/100)*tempo)
# valor = prestação / (1+(taxa/100)​×tempo)

import os 
os.system('cls')

prestacao = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite o valor da taxa: "))
tempo = int(input("Digite o tempo de atraso em meses: "))

# Formata para exibir duas casas depois da vírgula
# :.2f
valor = prestacao/(1+((taxa/100)*tempo))
print(f"O valor da prestação em atraso é: {valor:.2f}.")