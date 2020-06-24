from flask_restful import Resource


lista_habilidades = ['Flask','SQL','JAVA','POMBA']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades