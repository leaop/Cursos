#soma de numeros pares
soma = 0
cont = 0
'''
minha tentativa

for c in range(1,7):
    c = int(input('qual o numero?'))
    if c %2 ==0:
        soma += c
    print(soma)
'''

for c in range(1,7):
    num = int(input('Digite o {}º valor'.format(c)))
    if num % 2==0:
        soma += num
        cont += 1
print('A soma dos pares informados foi de {}'.format(soma))
