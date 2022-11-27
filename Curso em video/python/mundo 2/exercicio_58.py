import random
from time import sleep
computador = random.randint(0,10)
print('Acabei de pensar em um numero entre 0 e 10')
sleep(0.1)
print('Tente advinhar')
acertou =  False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um numero maior')
        else:
            print('Tente um numero menor')
   
print('Parabens, dessa vez voce acertou com {} palpites'.format(palpite))