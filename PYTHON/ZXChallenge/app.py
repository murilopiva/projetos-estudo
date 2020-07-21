import json

import shapefile
from flask import Flask, request
from flask_restful import Resource, Api

from geojson import dumps, MultiPolygon, Polygon, Point
from shapely.geometry import shape

from models import Partners, init_db

app = Flask(__name__)
api = Api(app)


class Partinsert(Resource):
    def post(self):
        dados = request.json

        x = dumps(dados['coverageArea'])
        # x = x.replace('{', '')
        # x = x.replace('}', '')
        # x = json.dumps(x.replace('"', ''))

        y = dumps(dados['address'])
        # y = y.replace('{', '')
        # y = y.replace('}', '')
        # y = json.dumps(y.replace('"', ''))

        partner = Partners(tradingName=dados['tradingName']
                           , ownerName=dados['ownerName']
                           , document=dados['document']
                           , coverageArea=x
                           , address=y)  # id é gerado automaticamente
        partner.save()

        response = {
            'id': partner.id,
            'tradingName': partner.tradingName,
            'ownerName': partner.ownerName,
            'document': partner.document,
            'coverageArea': partner.coverageArea,
            'address': partner.address,
        }

        return response


class Partlist_all(Resource):
    def get(self):
        parts = Partners.query.all()
        response = [{'id': i.id,
                     'tradingName': i.tradingName,
                     'ownerName': i.ownerName,
                     'document': i.document,
                     'coverageArea': json.loads(i.coverageArea),
                     'address': json.loads(i.address),
                     } for i in parts]
        return response


class PartlistID(Resource):
    def get(self, id):
        parts = Partners.query.filter_by(id=id).first()

        try:
            response = {
                'id': parts.id,
                'tradingName': parts.tradingName,
                'ownerName': parts.ownerName,
                'document': parts.document,
                'coverageArea': json.loads(parts.coverageArea),
                'address': json.loads(parts.address),
            }
        except AttributeError:
            response = {
                'status': 'erro',
                'mensagem': 'Id não encontrado'
            }

        return response

    def delete(self, id):
        dele = Partners.query.filter_by(id=id).first()
        dele.delete()

        return {'status': 'sucesso'
            , 'mensagem': 'mensagem'}


api.add_resource(Partinsert, '/pst/')
api.add_resource(PartlistID, '/lst/<string:id>')
api.add_resource(Partlist_all, '/lst/')

x = MultiPolygon([(-38.6577, -3.7753),
                  (-38.63212, -3.81418),
                  (-38.61925, -3.82873),
                  (-38.59762, -3.84004),
                  (-38.58727, -3.84345),
                  (-38.58189, -3.8442),
                  (-38.57667, -3.84573),
                  (-38.56706, -3.85015),
                  (-38.56637, -3.84937),
                  (-38.56268, -3.84286),
                  (-38.56148, -3.83772),
                  (-38.55881, -3.82411),
                  (-38.55577, -3.81507),
                  (-38.55258, -3.80674),
                  (-38.54968, -3.80222),
                  (-38.53406, -3.79495),
                  (-38.52894, -3.77718),
                  (-38.52517, -3.76313),
                  (-38.53118, -3.76203),
                  (-38.53968, -3.76126),
                  (-38.54577, -3.76151),
                  (-38.55344, -3.76102),
                  (-38.56327, -3.76029),
                  (-38.58118, -3.75907),
                  (-38.60079, -3.75423),
                  (-38.60671, -3.74772),
                  (-38.61787, -3.7431),
                  (-38.62577, -3.7472),
                  (-38.63332, -3.7496),
                  (-38.65049, -3.76057),
                  (-38.6577, -3.7753)])

#print(x.__contains__((-38.641, -3.77547)))
#https://geojsonlint.com/
#https://gis.stackexchange.com/questions/208546/check-if-a-point-falls-within-a-multipolygon-with-python
from shapely.geometry import MultiPolygon, Polygon



if __name__ == '__main__':
    init_db()
    app.run(debug=True)



"""
import matplotlib.pyplot as plt

coord = x['coordinates']
#coord.append(coord) #repeat the first point to create a 'closed loop'

xs, ys = zip(*coord) #create lists of x and y values

plt.figure()
plt.plot(xs,ys)
plt.plot((-38.6577, -3.7753),(-38.641,-38.649), (-3.77547,-3.77542),(-38.6577, -3.7753))
#plt.show() # if you need...



"""