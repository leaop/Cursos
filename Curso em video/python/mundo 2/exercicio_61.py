#PA
print('Gerador de PA')
print('-='*10)
p =  int(input('Primeiro termo: '))
r = int(input('Razão da PA '))
t = p
cont = 1
while cont<=10:
    print('{} >'.format(t), end='')
    t += r
    cont += 1
print('FIM')