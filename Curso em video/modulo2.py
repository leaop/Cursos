"""
#aula 01

#soma de dois valores imprimidos segundo a interacao
a = int(input('Digite o primeiro numero: '))
b = int(input("Digite o segundo valor: "))
s = a + b
#aqui as chaves vao ser preenchidas pelo .format()
print('A soma entre', a,'e',b, 'vale {}'.format(s))
#as chaves são mascaras que foram preenchidos por um metodo
#o codigo de cima tambem pode ser:
#print("A soma entre {} e {} vale {}".format(a, b, s))
#aqui eu tenho que colocar o valor de cada mascara
"""
"""
#aula 02

# Faça um programa que leia algo do teclado e mostre o tipo desse algo
a = input('Digite algo para saber seu tipo: ')
print("O tipo do que digitou acima é:", type(a))
#o problema desse metodo é o que o input sempre retorna uma str
#a partir desse problema temos a seguinte opcao
print( 'É numero?', a.isnumeric())
print('Tem somente espaços?', a.isspace())
print('É alfabético? ', a.isalpha())
print('É alfanumérico', a.isalnum())
#temos tambem a funçao isupper e islower
"""
#aula 03
#ordem de precedencia
#1 ()
#2 **
#3 *, /, //, %
#4 +, -
print(5+2)
#Faça um programa que leia o numero inteiro e mostre a tela o seu antecessor e seu sucessor
#Faça outro programa que mostre o dobro, o triplo e a raiz quadrada de um numero
#desenvolva um progrma que leia as duas notas de um aluno e mostre a sua média
#Escreva um programa que leia a medida em metros e a converta para centimetros e milimetros
#Faça um programa que elabora a tabuada de um numero colocado (interação)
#Crie um programa que leia qunato dinheito uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Faça um programa que leia a altura e a largura de uma parede e calcula sua area e a quantidade de tinta para pinta-la
#para o desafio anterior considere que um litro de tinta, pinta 2m²
#Faça um algoritmo que leia o saladio de um funcionário e mostre o mesmo com um aumento de 15%