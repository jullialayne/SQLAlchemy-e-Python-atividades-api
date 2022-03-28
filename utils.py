from models import Pessoas,db_session

#Insere dados na tabela pessoa
def insere_pessoas(pessoa):
    pessoa.save()

#Consulta dados na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

#Altera dados na tabela pessoa
def altera_pessoa(pessoa,nome1):
    pessoa = Pessoas.query.filter_by(nome=pessoa.nome).first()
    pessoa.nome=nome1
    pessoa.save()

#Exclui dados na tabela pessoa
def exclui_pessoa(nome1):
    pessoa = Pessoas.query.filter_by(nome=nome1).first()
    pessoa.delete()

if __name__ == '__main__':

    #simulaçoes
    pessoa = Pessoas(nome='Layne', idade=22)
    nome1='Junia'
    
    insere_pessoas(pessoa)
    altera_pessoa(pessoa,nome1)
    exclui_pessoa(nome1)
    consulta_pessoas()
