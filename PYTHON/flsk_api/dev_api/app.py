from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'nome': 'Murilo',
        'habilidades': ['Python', 'Flask'] },
    {
        'nome': 'Piva',
        'habilidades': ['SQL', 'Django']}
]

#devolve um desenvolvedor pelo ID, altera e deleta também
@app.route("/dev/<int:id>/", methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            msg = 'Desenvolvedor de ID {} não existe!'.format(id)
            response = {'status':'erro','mensagem':msg}
        except Exception:
            msg = 'Erro desconhecido. Procure o ADM da API'
            response = {'status':'erro','mensagem':msg}

        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem':'Registro excluido'})

#lista todos e inclui um nove
@app.route('/dev/',methods=['POST','GET'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)
