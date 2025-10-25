# Algoritmo 46
# Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima o novo saldo, considerando o reajuste de 1%

import os
os.system('cls')

saldoIni = float(input("Digite o saldo inicial: "))

reaj = 0.01
valorReaj = reaj * saldoIni
saldoFim = saldoIni + valorReaj

print(f"Saldo inicial: {saldoIni}\nValor do reajuste: {valorReaj}\nSaldo final: {saldoFim}")