import os
os.system('clear')

# Tupla
# Não é possível alterar o valor da tupla

# Sinaxe básica da tupla

tupla = (1,2)
print(tupla)

# Tupla com um um único elemento
tupla = (5,)
print(tupla)

# Tupla com vários elementos
tupla = (1, 2, 3, 4, 5)
print(tupla)

# Acessando elementos da tupla por índice
tupla = (10, 20, 30, 40)

# Acessando o terceiro elemento (índice 2)
print(tupla[2])

# Contando a quantidade de vezes um valor aparece na tupla
tupla = (1, 2, 2, 3, 4, 2)
print("Quantas vezes o número dois aparece: ", tupla.count(2))

# Contando a quantidade de vezes um valor aparece na tupla (também funciona para string)
tupla = ("iPhone", "Samsung","iPod","iPod","Samsung","iPhone")
print("Quantos iPhones tenho no estoque: ", tupla.count("iPhone"))

# tupla dentro de uma tupla (tupla aninhada)
tupla = ((1,2),(3,4),(5,6))
# Acessando a segunda tupla (3,4)
print(tupla[1])

# Encontrando o índice de um valor na tupla
tupla = (10, 20, 30, 40)
# Encontrando o índice do número 30
print(tupla.index(30))


# Desempacotando os valores de uma tupla
tupla = (1,2,3)
# Atribuindo um valor a cada variável
a, b, c = tupla
print(a,b,c)