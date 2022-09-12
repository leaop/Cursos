# a ideia de hoje é fazer o mesmo registro da aula passada(pacientes) com programacao orientada a objetos
# logica de relacao entre funcao e variável
"""Classe, objeto e construtor"""
class Paciente:
# Paciente - conjunto de objetos que compartilham de caracteristicas similares
    #pass
# O construtor é uma função com o mesmo nome da classe que é criado internamente pelo python
# Como eu sei que foi criado? pela linha de código: <paciente.Pciente object at 0x7fc65739bb0
# esse ultimo código é uma linha de memória
# instanciar objeto =  passar o valor do objeto para um variável, tendo maior controle sobre ela
    def __init__(self):
        print("Acessei o paciente")