'''Algoritmo 48
Antes de o racionamento de energia ser decretado, quase ninguém falava em
quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário.

Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo,
fazer um algoritmo que receba o valor do salário mínimo e a quantidade de
quilowatts gasta por uma residência e calcule. Imprima:
O valor em reais de cada quilowatt
O valor em reais a ser pago
O novo valor a ser pago por essa residência com um desconto de 10%.'''

salarioMinimo = float(input("Digite o valor do salário mínimo: "))
gastoResid = int(input("Digite a quantidade de quilowatts gasta pela residência: "))

kw = 100
teste = salarioMinimo / 7

cemKW = kw * (salarioMinimo / 7)
print(f"Teste: {teste}")
print(f"Cem quilowatts custam: {cemKW}")


# print(f"Valor em reais de cada quilowatt: {}")






