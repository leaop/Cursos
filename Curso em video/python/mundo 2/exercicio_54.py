#idade de pessoas
from datetime import date
atual = date.today().year
totm = 0
tot = 0
for pess in range (1,8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totm += 1
    else:
       tot += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totm))
print('E tambem tivemos {} pessoas menores de idade'.format(tot))