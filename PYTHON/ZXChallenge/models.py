from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

engine = create_engine('sqlite:///comp.db', convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

#engine.execute("drop table if exists partner")

# criar tabelas
# tabelas são classes

class Partners(Base):
    __tablename__ = 'partners'
    id = Column(Integer, primary_key=True)
    tradingName = Column(String(40), index=True)  # cria index
    ownerName = Column(String(40))
    document = Column(String(40), unique=True)
    coverageArea = Column(String(10000))
    address = Column(String(2000))

    # representa o objeto
    def __repr__(self):
        return '<Partner {}'.format(self.tradingName)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    # create_all é quem cria o banco
    Base.metadata.create_all(bind=engine)
#
# if __name__ == '__main__':
#     init_db()
