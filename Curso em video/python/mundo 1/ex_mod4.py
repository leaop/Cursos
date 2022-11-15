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

#Lendo a velocidade de um carro e aplicando multa
velo = float(input('Qual a velocidade que está andando?'))
if velo > 80:
    print('Multado! voce excedeu o limite de velocidade da via de 80km/h')
    multa = (velo-80) *7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia')

#mostre se o numero é par ou impar
num = int(input('Me diga um numero qualquer:'))
resultado = num%2
if resultado == 0:
    print('O numero {}, é PAR',format(num))
else:
    print('O numero {}, é IMPAR'.format(num))

#Calcular o preço da passagem com base na distancia (até 200km, cobra 0,5. Após essa distancia: 0,45)
dist = int(input('Qual a distancia da velocidade'))
if dist <= 200:
    price = dist* 0.50
else:
    price = dist*0.45
'''price  = dist * 0.5 if dist <= 200 else dist * 0.45'''
print("E o preço da sua passagem será de R${:.2f}".format(price)) 

#Ano bissexto
from datetime import date
ano = int(input('Qual ano quer analisar? Ou coloque 0 para o ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('Esse ano de {} não é bissexto'.format(ano))

#Qual a ordem dos valores
a = int(input('Primeiro valor'))
b = int(input('Segundo valor'))
c = int(input('Terceiro valor'))
'''if a<b and a<c: menor = a .... e assim por diante'''
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor foi {}.'.format(menor))
print('O maior valor foi{}.'.format(maior))

#formação de triangulo
r1 = float(input('Primeiro segmento'))
r2 = float(input('Segundo segmento'))
r3 = float(input('Terceiro segmento'))
if r1 < r2+r3 and r2<r1+r3 and r3<r2+r2:
    print('Esses segmentos formam um triangulo')
else:
    print('Não foi possivel formar um triangulo')