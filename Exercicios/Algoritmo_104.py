# Algoritmo 104
# Entrar com nome, sexo e idade de uma pessoa. Se a pessoa for do sexo
# feminino e tiver menos que 25 anos, imprimir nome e a mensagem: ACEITA.
# Caso contrário, imprimir nome e a mensagem: NÃO ACEITA. (Considerar f ou
# F.)

import os
os.system('clear')

nome = input(input("Digite o nome: "))
sexo = input("Digite o sexo: ")
idade = int(input("Digite a idade: "))

# Formata a string em minúsculas
sexo = sexo.lower() 

if(sexo == 'f' and idade < 25):
    print("ACEITA")
else:
    print("NÃO ACEITA")