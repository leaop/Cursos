#contagem regressiva de 10
from time import sleep
#o L é a variável de controle
#sempre coloca um numero a mais ou a menos do que quer
for l in range(10, -1, -1):# vai da ordem inversa, tirando -1
    print(l)
    sleep(2)
print('BOM! BUM! POW!')