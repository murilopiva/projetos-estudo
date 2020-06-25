from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

#api rest de pessoas
class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError:
            response = {'status':'erro','Mensagem':'Pessoa não encontrada'}

        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome = nome).first()
        dados = request.json

        if 'nome' in dados:
            pessoa.nome = dados['nome']

        if 'idade' in dados:
            pessoa.idade = dados['idade']

        if 'id' in dados:
            pessoa.id = dados['id']

        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome ,
            'idade':pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluída com sucesso'.format((pessoa.nome))
        pessoa.delete()
        return {'status':'sucesso','mensagem':mensagem}


class Listapessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i .nome, 'idade': i.idade} for i in pessoas]
        #print(response)
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade']) # id é gerado automaticamente
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome ,
            'idade':pessoa.idade
        }
        return response


class Listaatividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'Pessoa': i.pessoa.nome} for i in atividades]
        #print(response)
        return response

    def post(self):
        dados = request.json
        try:
            pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
            atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
            atividade.save()
            response = {
                'pessoa': atividade.pessoa.nome,
                'atividade': atividade.nome,
                'id': atividade.id
            }
        except AttributeError:
            response = {'status':'erro','Mensagem':'Pessoa não encontrada'}

    def delete(self, id):
        atv = Atividades.query.filter_by(id=id).first()
        mensagem = 'Atv {} excluída com sucesso'.format((atv.nome))
        atv.delete()
        return {'status': 'sucesso', 'mensagem': mensagem}

        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(Listapessoas, '/pessoa/')
api.add_resource(Listaatividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)

