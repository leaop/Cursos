r1 = input(int('Primeiro segmento:'))
r2 = input(int('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 < r3 < r1 + r2:
    print('Os segmento podem formar um triangulo', end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Esses segmentos não formam um triangulo')

