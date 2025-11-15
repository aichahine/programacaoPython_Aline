''' Algoritmo 98
A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
estatutários. O valor máximo da prestação não poderá ultrapassar 30% do
salário bruto.
Fazer um algoritmo que permita entrar com o salário bruto e o valor
da prestação e informar se o empréstimo pode ou não ser concedido. '''

import os
os.system('cls')

salario = float(input("Digite o valor do salário: "))
prestacao = float(input("Digite o valor da prestação: "))

valorMaximo = salario * (30/100)

if(prestacao < valorMaximo):
  print(f"\nSalário: R$ {salario}\nPrestação: R$ {prestacao}\nEmpréstimo concedido.")
else:
  print(f"\nSalário: R$ {salario}\nPrestação: R$ {prestacao}\nValor máximo: R$ {valorMaximo}\nEmpréstimo negado.")