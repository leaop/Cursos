n = int(input('Digite um numero para calcular o fatorial'))
c = n
f = 1
while c>0:
    print('{}'.format(c), end='')
    print('x' if c>1 else '=', end='')
    c -= 1
print('O fatorial de {} é {}'.format(n, f))