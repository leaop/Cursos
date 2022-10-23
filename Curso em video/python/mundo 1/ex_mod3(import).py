#crie um programa que leia um numero real qualquer pelo tecaldo oe mostre na tela a sua porção inteira
#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
#um professor deseja fazer um sorteio entre os alunos, faça um porgrama que o ajude
#faça um programa que faça uma ordem aleatoria entre 4 alunos
#faça um programa que leia um arquivo mp3()
from distutils.command.sdist import sdist
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua proção inteira é {}'.format(num, math.trunc(num))))
#ou
num2 = float(int('Digite um valor: '))
print('O valor digitado foi {} e sua porcao itneiro é {}'.format(num2,int(num2)))
#from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co**2 + ca**2)**2 #math.hypot(co,ca)
print('A hipotenusa vai medir{:.2f}'.format(hi))

#seno, cos, tang
#from math import radians, sin, cos, tan (essa linha elimina o math. das seguintes)
an = float(input("Digite o angulo que voce deseja: "))
seno = math.sin(math.radinas(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O angulo de {} tem o SENO de {}, o COSSENO de {} e a TANGENTE de{}'.format(an, seno, cosseno, tangente))

#os alunos sorteados
import random
#from random import choice, shuffle
n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista=[n1, n2, n3, n4]
escolhido = random.choice(lista)
present = random.shuffle(lista)
print('O aluno escolhido parar iniciar a apresentação foi {}'.format(escolhido))
print('A ordem de apresentação vai ser {}'.format(present))

#tocando mp3
#algumas bibliotecas que fazem isso: playsound, pygame, vlx, webbrowser, os
#é preciso que o arquivo mp3 esteja na mesma pasta do arquivo python
import pygame
pygame.init()
pygame.mixer.music.load('nome do arquivo')
pygame.mixer.music.play()
pygame.event.wait()

