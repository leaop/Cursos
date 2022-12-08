#soma com condiçao de parada
#vamos usar um conceito de flag
#flag é um sinal(por isso o nome) para determinar se determinada sessão deve ser executada ou não
#é construido a partir da repetição do comando dentro e fora da repetição
"""n = cont = soma = 0
n = int(input('Digite um numero [999 para parar]': ))#flag
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero [999 faz parar]: '))
print('Voce digitou {} numeros e a soma é de {}'.format(cont,soma))
"""
#o codigo acima funciona, mas parece uma 'gambiarra'
#o mais adequado para o caso é usar loop infinito + break condicional
n = s = 0
while True:#loop infinito
    n = int(input('Digite um numero: '))
    if n == 999:
        break#condicional: se o numero for a condição, o loop para
    s += n
print(f'A soma valor {s}')#formato do Py 3.6+
