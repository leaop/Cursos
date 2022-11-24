#soma de todos os numeros entre 1 e 500, que são multiplos de 3
#acumuladores
soma = 0
cont = 1
for c in range(1,501, 2):
    if c % 3 ==0:
        cont += 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
    