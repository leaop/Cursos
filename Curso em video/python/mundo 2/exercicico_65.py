resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite o numero:'))#coloque um valor
    quant += 1 #a quantidade sempre vai ser esse valor + outros que colocar
    soma += num #a soma vai ser os numeros que colocarem, pq vai ser um numero mais o outro
    if quant == 1: #caso só tenha um numero
        maior = menor = num #esse numero vai ser o menor e o maior
    else: #se tiver mais de um
        if num > maior: # o numero maior vai ser o maior
            maior = num
        if num < menor: # o numero menor tem que ser menor que o menor
            menor = num
    resp = str(input('Quer continuar? [S/N')).upper().strip()[0]#interação: tudo em maiusculo, sem espaço (inclusive depois de acabar)
media = soma/quant#tem que ser fora para esperar o loop acabar
print('Voce digitou {} numeros e a media foi de {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))


