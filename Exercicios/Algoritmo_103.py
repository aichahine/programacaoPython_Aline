# Algoritmo 103
# Entrar com o ano de nascimento de uma pessoa e o ano atual. Imprimir a idade
# da pessoa. Não se esqueça de verificar se o ano de nascimento é um ano
# válido

import os
os.system('clear')

anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

if(anoNascimento>anoAtual):
    print(f"Ano de nascimento inválido")
else:
    print(f"Ano de nascimento válido")

idade = anoAtual - anoNascimento
print(f"A idade é: {idade} anos.")