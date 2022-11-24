#mostrar na tela os numeros de 1 a 50 que são pares
from time import sleep
for p in range(1,51):# alternativa seria pedir para pular de 2 em 2, iniciando no par
    if p % 2 == 0:
        print(p)
        sleep(0.2)
print('Pronto, todos os pares')
#a alternativa é melhor pois tem menos movimentos a se fazer