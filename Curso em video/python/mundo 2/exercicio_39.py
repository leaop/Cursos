from datetime import date
ano = date.today().year
nasc = int(input('Qual o ano do seu nascimento?'))
idade = ano - nasc
alis =  18 - idade
print('Quem nasceu em {} tem {} em {}'.format(nasc, idade, ano))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    #poderia ter colocado a alis aqui
    print('Voce ainda nao tem 18 anos. Ainda faltam {} anos para o alistamento'.format(alis))
elif idade > 18:
    #assim como o alis poderia estar dentro da outra, aqui poderia estar uma variável saldo = idade - 18 para dizer a quantos anos deveria ter se alistado
    print('Voce já deveria ter se alistado')
