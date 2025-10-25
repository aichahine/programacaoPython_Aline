'''Algoritmo 48
Antes de o racionamento de energia ser decretado, quase ninguém falava em
quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário.

Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo,
fazer um algoritmo que receba o valor do salário mínimo e a quantidade de
quilowatts gasta por uma residência e calcule. Imprima:
O valor em reais de cada quilowatt
O valor em reais a ser pago
O novo valor a ser pago por essa residência com um desconto de 10%.'''

import os 
os.system('cls')

salarioMinimo = float(input("Digite o valor do salário mínimo: "))
gastoResid = int(input("Digite a quantidade de quilowatts gasta pela residência: "))

setimo = salarioMinimo / 7
valorkw = setimo / 100

pagar = valorkw * gastoResid
desconto = pagar * 0.10
novoValor = pagar - desconto

print(f"O valor de um sétimo do saláriom mínimo é: R${setimo}")
print(f"O valor em reais de cada quilowatt: R${valorkw}")
print(f"O valor em reais a ser pago: R${pagar}")
print(f"O novo valor a ser pago por essa residência com um desconto de 10%: R${novoValor}")