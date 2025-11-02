''' Algoritmo 63
Criar um algoritmo que efetue o cálculo do salário líquido de um professor. Os dados fornecidos
 serão: valor da hora aula, número de aulas dadas no mês e percentual de desconto do INSS.'''

import os 
os.system('cls')

# Recebendo os valores
valorHoraAula = float(input("Digite o valor da hora aula: "))
numeroAulas = int(input("Digite o número de aulas dadas no mês: "))
inss = float(input("Digite o percentual de desconto do INSS: "))

salario = valorHoraAula * numeroAulas
desconto = salario * (inss / 100)
salarioLiquido = salario - desconto

print(f"O salário líquido é: {salarioLiquido}")