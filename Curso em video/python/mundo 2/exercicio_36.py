valor = float(input('Qual o valor da casa?'))
salario = float(input('Qual seu salário?'))
anos = int(input('Quantos anos pretende pagar?'))
prestação = valor/(anos*12)
if prestação <= salario*(30/100):
    print('podemos aprovar seu emprestimo')
else:
    print('infelizmente não podemos conceder o emprestimo')