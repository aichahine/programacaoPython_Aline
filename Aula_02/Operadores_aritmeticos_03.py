import os 
os.system('cls')

quantidade= 5
valor = 2800
desconto = 0.15

# primeira forma
total = quantidade*valor
desconto = total*desconto
valorFinal = total - desconto

# f {} é uma forma de exibir 
print(f"total: {valorFinal}")
print(f"Total de desconto: {total}")

# segunda forma
total02 = quantidade *(valor - ((valor/100)*15))
print(total02)
