# UTILS É APENAS PARA ANTES DE FAZER O RESTful COM O APP.PY

import sqlite3

from models import Partners
from geojson import GeometryCollection, Point, LineString, MultiPolygon, Feature, dumps

# x = MultiPolygon([
# ([(3.78, 9.28), (-130.91, 1.52), (35.12, 72.234), (3.78, 9.28)],),
# ([(23.18, -34.29), (-1.31, -4.61), (3.41, 77.91), (23.18, -34.29)],)
# ])  # doctest: +ELLIPSIS
#
# geo_collection = GeometryCollection([x])
# # print(geo_collection)
# geo_collection[1]


my_point = MultiPolygon([
    ([(3.78, 9.28), (-130.91, 1.52), (35.12, 72.234), (3.78, 9.28)],),
    ([(23.18, -34.29), (-1.31, -4.61), (3.41, 77.91), (23.18, -34.29)],)
])  # doctest: +ELLIPSIS

dump = dumps(my_point)


print(dump)


# from geojson import Point, Feature, FeatureCollection, dump
#
# point = Point((-115.81, 37.24))
#
# features = []
# features.append(Feature(geometry=point, properties={"country": "Spain"}))
#
# # add more features...
# # features.append(...)
#
# feature_collection = FeatureCollection(features)
# print(feature_collection)

def inclusao():
    x = MultiPolygon([(((0, 0), (0, 3), (3, 3), (3, 2 - 2), (2, 2 - 2), (2, 2), (1, 2), (1, 1), (2, 1), (2, 1 + 1),
                        (3, 1 + 2), (3, 0), (0, 0)),
                       [((2, 2), (1 - 1, 1), (1 - 2, 1 - 1), (2, 1 - 1), (1, 2))])
                      ])

    # print(dumps(x))

    part = Partners(tradingName='murilo'
                    , ownerName='piva'
                    , document='oi'
                    , coverageArea=str(x)
                    , address='oi'
                    )

    part.save()


# consulta
def consulta_pessoas():
    part = Partners.query.filter_by(tradingName='murilo').first()
    print(part)


# para deletar, tem que criar outro metodo na classe Pessoas, não pode usar o .save que é commit
def exclui_partner():
    partner = Partners.query.filter_by(tradingName='murilo')
    partner.delete()


if __name__ == '__main__':
    # exclui_partner()
    # inclusao()
    consulta_pessoas()
