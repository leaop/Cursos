#jogo de advinhação
import random as rd
from time import sleep
num = rd.randint(0,5)
print('Vou pensar em um numero entre 0 e 5, tente advinhar')
resp = int(input('Em que numero eu pensei?'))
print('Processando...')
sleep(1)
if resp == num:
    print('voce ganhou')
else:
    print('tente na proxima, eu pensei no numero {}'.format(num))

#