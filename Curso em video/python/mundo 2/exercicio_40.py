nota1 = float(input('Primeira nota'))
nota2 = float(input('Segunda nota'))
media = (nota1 + nota2)/2
print('Sua média foi de: {}'.format(media))
if 7> media and media <7:
    print('O aluno está em recuperação')
elif media <5:
    print('O aluno está reprovado')
else:
    print('O aluno foi aprovado')