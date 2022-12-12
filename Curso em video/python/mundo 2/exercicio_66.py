n = s = cont = 0
while True:
    n = int(input('Digite o numero (999 para):'))
    if n == 999: # precisa estar aqui para que antes de seguir, ele verifique se o 999 apareceu
        break
    s += n
    cont += 1
print(f'A soma dos {cont} valores foi de {s}')