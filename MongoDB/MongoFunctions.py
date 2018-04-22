from pymongo import MongoClient
from datetime import datetime

class MongoFunctions:

    def __init__(self):
        pass

    def registrar_logs(self,login,ip):
        try:
            client = MongoClient("127.0.0.1")
            db = client["itep"]
            db.itep.insert({"login":login,"ip":ip,"data":datetime.now()})
        except Exception as e:
            print "Erro: %s"%e

    def listar_ultimos_acessos(self):
        try:
            client = MongoClient("127.0.0.1")
            db = client["itep"]
            db.itep.find({})
            for i in db.itep.find().limit(5):
                print i["login"]," - ",i["ip"]," - ",i["data"]
        except Exception as e:
            print "Erro: %s"%e

