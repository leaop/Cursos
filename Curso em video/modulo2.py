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
