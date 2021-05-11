from models import Pessoas,db_session

#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Layne', idade=22)
    print(pessoa)
    pessoa.save()

#Consulta dados na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #pessoa = Pessoas.query.filter_by(nome='Jullia').first()
    #print(pessoa.idade)

#Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Layne').first()
    pessoa.nome='Junia'
    pessoa.save()

#Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Junia').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
