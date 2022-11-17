from datetime import date
ano = date.today().year
nasc = int(input('Qual o ano do seu nascimento?'))
idade = ano - nasc
print('Quem nasceu em {} tem {} em {}'.format(nasc, idade, ano))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')
