n = int(input('Digite um numero: '))
t = 0
for c in range(1,n+1):
    if n % c ==0:
        print('\033[34m', end='')
        t += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO numero {} foi dividisvel {} vezes'.format(n, t))
if t == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')