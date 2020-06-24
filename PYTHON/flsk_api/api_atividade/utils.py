from models import Pessoas

#insere
def insere_pessoas():
    pessoa = Pessoas(nome='Piva', idade=25)
    print(pessoa)# vai printar murilo pq defini o metodo __repr__ da classe Pessoas, em models, para retornar o nome do obj
    #db_session.add(pessoa)
    #db_session.commit()
    pessoa.save() # ao invés de usar as duas linhas comentadas acima, foi criado o metodo save na classe pessoa que já commita a nova pessoa criada


#consulta
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

    #usando filter_by vai trazer uma lista então tem que fazer um for (for i in pessoa: print(I)
    #então, eu uso o .first() para pegar o primeiro obj
    pessoa = Pessoas.query.filter_by(nome='Piva').first()

    #print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Piva').first()
    pessoa.idade = 30
    #caso eu queira alterar outra coluna
    #pessoa.nome = 'POMBA'
    pessoa.save()

#para deletar, tem que criar outro metodo na classe Pessoas, não pode usar o .save que é commit
def exclui_pessoa():
    pessoas = Pessoas.query.filter_by(nome='Murilo').first()
    pessoas.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()



