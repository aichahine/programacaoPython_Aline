'''
for:      Esta palavra-chave inicia o loop. É usada para iterar sobre uma sequência.
i:        Este é o nome da variável de controle do loop. Em cada iteração do loop, 
          i irá assumir o valor de cada elemento na sequência que está sendo iterada (neste caso, lista_compras).
in:       Esta palavra-chave é usada para indicar que estamos iterando sobre os elementos de uma sequência.
          lista_compras: Esta é a sequência que estamos iterando. Pode ser uma lista de itens de compras,
          por exemplo: lista_compras = ['maçã', 'banana', 'leite'].
print(i): Este é o corpo do loop, que é executado em cada iteração. A função print(i) imprime o valor atual de i, que é o elemento atual da lista.

Quando o código é executado, o Python percorre cada item na lista_compras.
Para cada item, ele atribui o valor à variável i e, em seguida, executa a instrução print(i).
Isso resulta na impressão de cada item da lista, um por um.

Exemplo Prático
Se lista_compras contiver os itens ['maçã', 'banana', 'leite'], a saída do código será:

maçã
banana
leite
'''
import os
os.system('clear')
import time

lista_compras = ["maçã","banana","leite"]

for i in lista_compras:
        print(i)
        time.sleep(0.5)