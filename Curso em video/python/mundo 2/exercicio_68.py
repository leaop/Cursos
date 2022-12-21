v = 0
while True:
    jog = int(input('diga um valor de 0 a 10'))
    comp = randint(0,11)
    tot =  jog + comp
    tipo = ''
    while tipo not in 'PI':
        tipo = srt(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jog} e o computador {comp}, com um total de {tot}')
    if tipo == 'P':
        if tot %2==0:
            print('Voce GANHOU')
            v += 1
        else:
            print('voce PERDEU')
            break
    elif tot == 'I':
        if tot %2==1:
            print('voce GANHOU')
            v += 1
        else:
            print('voce PERDEU')
            break