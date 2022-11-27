somaidade=0
midade=0
midadeh=0
nvelho=''
tmulher =0
for p in range (1,5):
    print('-----{}ª PESSOA -----'.format(p))
    nome =  str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p==1 and sexo in 'Mm':
        midadeh == idade
        nvelho == nome
    if sexo in 'Mm' and idade > midadeh:
        midadeh == idade
        nvelho == nome
    if sexo in 'Ff' and idade<20:
        tmulher +=1
midade = somaidade/4
print('A media de idade do grupo é de {} anos'.format(midade))
print('O homem mais velho tem {} anos e se chama {}'.format(midadeh, nvelho))
print('Existe(m) {} mulher(s) com menos de 20 anos'.format(tmulher))