from Modulos.SSH import SSH
import json

class Docker(SSH):
    def __init__(self):
        self.image = "webservercloud"
        SSH.__init__(self)

    def criarContainer(self,nome):
        comando = "docker run -tdi --name %s --hostname %s %s /bin/bash"%(nome,nome,self.image)
        return self.executarComandoRemoto(comando)

    def pegarIPContainer(self,nome):
        comando = "docker inspect %s"%nome
        return json.loads(self.executarComandoRemoto(comando))[0]['NetworkSettings']['Networks']['bridge']['IPAddress']

    def acessarContainer(self,nome,comando):
        comando = "docker exec %s /bin/bash -c '%s'"%(nome,comando)
        return self.executarComandoRemoto(comando)

    def removerContainer(self,nome):
        comando = "docker stop %s && docker rm %s"%(nome,nome)
        return self.executarComandoRemoto(comando)

