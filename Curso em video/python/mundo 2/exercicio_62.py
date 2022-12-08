
print('Gerador de PA')
print('-='*10)
p =  int(input('Primeiro termo: '))
r = int(input('Razão da PA '))
t = p
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont<=10:
        print('{} >'.format(t), end='')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('Qunatos termos voce quer mostrar a mais? '))
print('Progresso finalizado com {} termos mostrados'.format(total))
