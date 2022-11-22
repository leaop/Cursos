from random import randint
import time
jg = ('Pedra', 'Papel', 'Tesoura')
print('O jogo se chama JO-KEN-PO')
print('''Escolha uma das opções:
[1] Pedra
[2] Papel
[3] Tesoura''')
op = int(input('Qual a sua jogada?'))
comp = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('O computador escolher {}'.format(jg[comp]))
if comp ==0:
    if op ==0:
        print('Empate')
    elif op==1:
        print('Voce ganhou')
    elif op==2:
        print('Voce perdeu')
    else:
        print('jogada invalida')
elif comp ==1:
    if op ==1:
        print('Empate')
    elif op == 0:
        print( 'Voce ganhou')
    elif op == 2: 
        print('voce perdeu')
    else:
        print('jogada invalida')
elif comp == 2:
    if op == 2:
        print('Empate')
    elif op == 0:
        print('Voce ganhou')
    elif op == 1:
        print('Voce perdeu')
    else:
        print('jogada invalida')