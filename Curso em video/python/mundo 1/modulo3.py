#modulos
"assim como a alimentaocao do corpo humano tem categorias, cada import é uma categoria e dentro da categoria temos itens"
#o math é um modulo que tra uma funcao a mais para funcoes matemáticas já presentes nativamente
import math
import random
num = random.randint(1,10000)
raiz = math.sqrt(num)
print('A raiz do {} é igual a {}'.format(num, raiz))

"""Modulo 3 - part 2 - aula 9"""
#cadeia de caracteres
"""Fateamento
Frase =  'Curso em video Python'
print('frase')
frase[9] <- somente o elemento do indice 9
indice <- começa no 0 e conta tambem os espaços, finalizando no 20
frase[9:21] <- vai pegar do elemento 9 até o 20(o ultimo nunca conta)
frase[9:13:2] <- ele vai comecar no 9 e vai até o 12, pulando de 2 em 2
frase[:5] <- é a mesma coisa que escrever do inicio até o elemento 4
frase[15:] <- vai do 15 até o final
frase(9::3) <- vai começar do 9 e vai até o final, pulando de 3 em 3
"""
"""Analise
frase.count('o') <- conta em toda extensao quantos elementos 'o' tem
frase.count('o', 0, 13) <- conta o 'o' do elemento 0 ao 12
frase.find('deo') <- procura o elemento entre aspas
se colocar um elemento de busca inexistente, o retorno será -1 e não um aviso de erro
"""
"""Transformação
frase.replace('Python', 'Android') <- substituição
frase.upper()<- método que troca o que é minusculo por maiusculo
frase.lower()<- a mesma coisa do upper, só que inverso
frase.capitalize() <- coloca tudo em minusculo, com exceção do primeiro
frase.title() <- transforma toda a primeira letra da palavra em maiuscula
frase.strip() <- remove os espaços no inicio e no final
frase.rstrip <- remove os espaços do lado direito, e colocando lstrip, remove os da esquerda
frase.split()<- vai dividir a string em listas, confrome os espaço
'-'.join(frase)<- comando para: juntar todos os elementos que foram separados em uma string
"""