tot18 = totH = totM = 0

while True:
    idade - int(input('Idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >=18:
        tot18 +=1
    if sexo == 'M':
        totH +=1
    if sexo == 'F' and idade<20:
        totM += 1
    
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'total de pessoas com amis de 18 anos é de {tot18}')
print(f'ao todo temos {totH} homens e {totM} mulheres com menos de 20 anos')
print('Acabou')