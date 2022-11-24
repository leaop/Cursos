#ler o primeiro termo, a razao da PA e mostres os 10 primeiros termos
p = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
d = p+(10-1)*r#essa é a formula do 10º termo da PA
for c in range(p,d+r,r):#se ficar só com p, tiraria 9 numeros
    print('{}'.format(c), end=' > ')
print('Acabou')