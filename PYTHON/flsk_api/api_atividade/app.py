from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

# apenas para demonstrar, vamos criar uma tabela de usuario
# USUARIOS = {
#     'murilo': '111',
#     'piva': '456'
# }

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

@auth.verify_password # verify password diz que a função abaixo é a que verifica senha
def verificacao(login, senha): # precisa explicitar quais metodos vao passar por verificação de senha, ver classe Pessoa
    # verifica se o login e senha foram mencionados
    # print('validando usuario')
    # print(USUARIOS.get(login)==senha)

    if not (login, senha):
        return False  # autenticação não foi feita com sucesso

    # else USUARIOS.get(login) == senha
    # posso deixar o else comentado acima porém posso já passar direto no return pq já vai retornar true ou false
    #return USUARIOS.get(login) == senha # se eu estivesse usando o dic de hardcode
    return Usuarios.query.filter_by(login=login,senha=senha).first() # usa o first pra retornar o obj. se não usar first, sempre retorna tru

# api rest de pessoas
class Pessoa(Resource):
    @auth.login_required # esse comando diz que precisa estar logado para acessar o metodo
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {'status': 'erro', 'Mensagem': 'Pessoa não encontrada'}

        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json

        if 'nome' in dados:
            pessoa.nome = dados['nome']

        if 'idade' in dados:
            pessoa.idade = dados['idade']

        if 'id' in dados:
            pessoa.id = dados['id']

        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluída com sucesso'.format((pessoa.nome))
        pessoa.delete()
        return {'status': 'sucesso', 'mensagem': mensagem}


class Listapessoas(Resource):
    @auth.login_required  # esse comando diz que precisa estar logado para acessar o metodo
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        # print(response)
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])  # id é gerado automaticamente
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class Listaatividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'Pessoa': i.pessoa.nome} for i in atividades]
        # print(response)
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
            response = {'status': 'erro', 'Mensagem': 'Pessoa não encontrada'}

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
