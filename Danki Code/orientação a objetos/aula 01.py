#como registrar vários pacientes sem ter que criar individualmente?

#criar uma função da receber os dados
def Registrar(nome, idade, cpf, email):
#vamos usar o dicionário por conta do controle mesmo, melhor do que tentar advinhar o index de lista
    paciente = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email}
# nao é preciso espeficiar o tipo, mas cria uma chave e uma variável que vai puxar o argumento 
    return paciente 