#crie um programa que leia um numero real qualquer pelo tecaldo oe mostre na tela a sua porção inteira
#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
#um professor deseja fazer um sorteio entre os alunos, faça um porgrama que o ajude
#faça um programa que faça uma ordem aleatoria entre 4 alunos
#faça um programa que leia um arquivo mp3()
import math
num = float(input('Digite um valor: ')
print('O valor digitado foi {} e a sua proção inteira é {}'.format(num, math.trunc(num))))
#ou
num2 = float(int('Digite um valor: '))
print('O valor digitado foi {} e sua porcao itneiro é {}'.format(num2,int(num2)))
#from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co**2 + ca**2)**2 #math.hypot(co,ca)
print('A hipotenusa vai medir{:.2f}'.format(hi))
