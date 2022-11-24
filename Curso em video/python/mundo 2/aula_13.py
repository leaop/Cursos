#estruturas de repetição
'''for c in range(1,6):
    print(c)
print('FIM')'''

i = int(input('Inicio: '))#primeiro numero
f = int(input('Fim: '))#ultimo numero
p = int(input('Passo: '))# de quantos em quantos anda
for c in range(i, f+1, p):#extensao da repetição
    print(c)
print('FIM')
