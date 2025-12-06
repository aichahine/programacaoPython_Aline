''' Nossa tarefa é verificar se há elementos duplicados em uma lista em algum lugar.
A primeira parte exigia que verificássemos se havia elementos duplicados em uma lista, um ao lado do outro.
Basta ordenar a lista e quaisquer duplicatas seriam encontradas na lista.
Você pode fazer um código que verifica a lista primeiro se há números adjacentes e, em seguida, você pode ordenar a lista e verificar.

for num in range(len(list) - 1):
if list[num] == range(num):
print ("true") '''

# https://www.reddit.com/r/learnpython/comments/12vy1fl/how_to_check_if_a_list_has_duplicate_elements/?tl=pt-br

import os
os.system('clear')

list = [1,1,4,6,4]
print(f"Lista: {list}")

for num in range(len(list)-1):

    if list[num]==range(num):
        print(f"True")