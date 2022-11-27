sx = str(input('Qual seu sexo [M/F]? ')).strip().upper()[0]
while sx not in 'MmFf':
    sx = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sx))