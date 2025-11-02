# Aula de 01 de novembro de 2025

# Infantil      0  - 11 >=0 and <=11
# Adolescente   12 - 17 >=12 and <=17
# Jovem         18 - 24 >=18 and <=24
# Adulto        25      >=25 and <=90

idade = int(input("Digite a idade: "))

#elif else if
if(idade>=0 and idade<=11):
    print("Infantil")
elif(idade >=12 and idade<=17):
    print("Adolescente")
elif(idade >=18 and idade<=24):
    print("Jovem")
elif(idade>=25 and idade<=90):
    print("Adulto")
else:
    print("Se você é jovem ainda, amanhã velho será")