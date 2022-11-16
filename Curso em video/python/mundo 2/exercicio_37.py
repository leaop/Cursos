num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversão:
[1] converter em binário
[2] converter para octal
[3] converter para hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('convertido para binário é igual a {}'.format(bin(num)[2:]))
elif opção == 2:
    print('convertido para octal é igual a {}'.format(oct(num)[2:]))
elif opção == 3:
    print('convertido para hexadecimal é igual a {}'.format(hex(num)[2:]))
else:
    print('tente outra opção')