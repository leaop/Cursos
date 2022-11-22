preco = int(input('Qual o valor da compra? '))
print('''Formas de pagamento:
[1] a vista
[2] 1x no cartão
[3] 2x no cartao
[4] 3x no cartao''')
op = int(input('Qual sua opção?'))
if op == 1:
    total =  preco - (preco * 10/100)
elif op == 2:
    total = preco - (preco * 5/100)
elif op == 3:
    total = preco
elif op == 4:
    total = preco + (preco * 20/100)
else:
    total = 0
    print('Opçao invalida de pagamento')
print('Sua compra terá o valor final de {}'.format(total))