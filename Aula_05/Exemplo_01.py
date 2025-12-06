''' Aula 05 - Listas

* As listas podem ser compostas por:
    - números [1,2,3,4]
    - letras ["A","B","C","D"]
    - tipos variados de dados ["A",35,'f',3.4] esta letra f refere-se ao char (true ou false)
    - compostas (matrizes) [
                            [1,2,3]
                            [4,5,6]
                            [7,8,9]
                                    ]

* Métodos:
    - append() adicionar
    - remove() remover
    - sort() ordenar

'''

# Criando uma lista

import os
os.system('clear')
import time

lista_compras = ["Arroz","Feijão","Açúcar","Leite"]
print(lista_compras)

for i in lista_compras:
    print(i)
    time.sleep(0.5)