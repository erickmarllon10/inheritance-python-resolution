from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Servidores(Base):
    __tablename__ = 'servidores'
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    endereco = Column(String)
    administrador = Column(String)

    def __init__(self,nome,endereco,administrador):
        self.nome = nome
        self.endereco = endereco
        self.administrador = administrador

if __name__ == '__main__':
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print "Erro: "%e
        session.rollback()



        
