#Faça um programa que leia o numero inteiro e mostre a tela o seu antecessor e seu sucessor
x = int(input("Digite um numero: "))
a = x+1
b = x-1
print(f'O seu numero é {x}, sendo precedido por {b} e tendo como sucessor {a}')
#print('Analisando o valor{}, o seu antecessor é{} e o seu sucessor é {}'.format(n, (n-1), (n+1)))

#Faça um programa que mostre o dobro, o triplo e a raiz quadrada
import math
from msilib import sequence
raiz = math.sqrt(x)#poderia tbm escrever x**0.5 ou math.pow()
print('tambem posso dizer que o dobro desse numero é ', x*2, 'o triplo é', x*3, 'e tem a raiz de', raiz )

#Faça um programa que leia as duas notas do aluno e de a média
nota1 = int(input("Qual foi sua primeira nota? "))
nota2 = int(input("E a segunda nota? "))
media = (nota1+nota2)/2
print("Com essas notas sua média é de", media)

#faça um programa que leia a media em metros, conversa para centimetros e milimetros
metro = float(input("Digite o metro: "))
print('Convertido para centrimetro é {} e em milimetros {}'.format((metro*100), (metro*1000)))

#Faça a tabuada de um numero colocado
import random
num = random.randint(1,100)
print('A tabuada vai ser de:',num)
print('-'*20)
for i in range(1,11):
    print("%d * %d = %d" % (num, i, num * i))
    #print("{} x {} = {}".format(num, i, num*i))
    #essa ultima linha pode ser feita uma por uma, colocando o multiplo no lugar do i
print('-'*20)

#Um programa que leia o dinheiro em conta e veja quanto o valor se equivale ao dolar
real = float(input('Quanto voce deseja trocar por dolar:? R$'))
dolar = real/3.27
print(f'Isso daria para comprar: U$${dolar}')
#print('Com R${:.2f} voce pode comprar U$${:.2f}'.format(real, dolar))

"""#ad do ultimo (cotação do dia)
import requests
import pandas as pd
from datetime import datetime
import time

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
"""

