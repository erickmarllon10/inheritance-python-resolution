from Usuarios.Usuarios import Users
from Servidores.Servidores import Servers
from MongoDB.MongoFunctions import MongoFunctions

def menu():
    lastaccess = MongoFunctions()
    lastaccess.listar_ultimos_acessos()
    print "\
            1 - Cadastrar Usuario: \n\
            2 - Acessar Sistema: \n\
            3 - Cadastrar Docker Container: \n\
            4 - Remover Docker Container: \n\
            5 - Acessar Docker Container: \n\
            6 - Definir Administrador: \n\
            7 - Alterar Senha: \n\
            8 - Sair: \n"

    opcao = input("Digite a sua opcao: ")
    return opcao

def switch(x):
    server = Servers()
    user = Users()
    dict_options = {1:user.cadastrar_usuario,
                    2:user.acessar_sistema,
                    3:server.cadastrar_container,
                    4:server.remover_container,
                    5:server.acessar_container,
                    6:server.definir_adm,
                    7:user.alterar_senha,
                    8:user.sair}
    dict_options[x]()

if __name__ == '__main__':
    try:
        while True:
            switch(menu())
    except Exception as e:
        print "Erro: "%e
