p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
op = 0
while op != 5:
    print(''' O que deseja fazer com os valores?
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
''')
    op = int(input('qual a sua opção? '))
    if op == 1:
        print(p + s)
    elif op == 2:
        print(p*s)
    elif op == 3:
        if p > s:
            print('O maior numero é {}'.format(p))
        else:
            print('O maior numero é {}'.format(s))
    elif op == 4:
        p = int(input('Qual seu novo numero? '))
        s = int(input('Qual é o segundo? '))
    elif op == 5:
        print('finalizado')
    else:
        print('Opção invávida, tente novamente')
print('fim do programa')   