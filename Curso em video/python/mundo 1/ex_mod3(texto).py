#nome completo com letas maiusculas, minusculas e a quantidade de letras do primeiro nome
nome = input('Qual seu nome completo? ').strip()#o input por padrão gera uma lista
print('Analisando seu nome...')
print('Seu nome completo em maiusculas é {}'.format(nome.upper()))
print('Seu nome completo em minusculas é {}'.format(nome.lower()))
print('O nome completo tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('E seu primeiro nome tem {} letras'format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Digite um numero:'))
#n = str(num)
print('Vamos analisar o numero {}'.format(num))
#print("Unidade: {}".format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))
u = num // 1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar; {}'.format(m))

#Um programa que leia o nome de uma pessoa que tenha SILVA
nome = str(input('Qual seu nome completo?')).strip() #para tirar os espaços
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
#oin é um operador que vai verificar a existencia do silva na string do nome

#Faça um program que leia uma frase e mostre quantas vezes temos a letra A e qual sua ultima posição
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição{}'.format(frase.find('A')+1))
print('A utima letra A aparece na posição {}'.format(frase.rfind('A')+1))

#Faça um rograma que leia o nome da pessoa e mostre o primeiro e o ultimo nome separadamente
nome = str(input('Digite seu nome: ')).strip()
n = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n)-1])
