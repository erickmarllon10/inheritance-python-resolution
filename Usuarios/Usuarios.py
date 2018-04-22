import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from Models.Model import Usuarios
from Models.Model import Servidores
from datetime import datetime

class Users:

    def __init__(self):
        pass

    def cadastrar_usuario(self):
        print "cadastro de usuarios"
        nomeUser = raw_input("Digite o nome do usuario: ")
        emailUser = raw_input("Digite o email do usuario %s: "%nomeUser)
        while True:
            senhaUser = raw_input("Digite a senha do usuario %s: "%nomeUser)
            senhaConfirm = raw_input("Digite a senha novamente: ")
            if senhaConfirm != senhaUser:
                print "As senhas nao coincidem"
            else:
                break
        userPass = session.query(Usuarios).filter(Usuarios.email==emailUser, Usuarios.senha==senhaUser).first()
        count = 1
        while count <=4:
            if userPass == None:
                senhaUser = raw_input("senha incorreta. Digite a senha novamente ou s para \"esqueci a senha\" (tentativa %s de 3): "%count)
                userPass = session.query(Usuarios).filter(Usuarios.email==emailUser, Usuarios.senha==senhaUser).first()
                count += 1

        try:
            engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            usuario = Usuarios(nomeUser, emailUser, senhaUser)
            session.add(usuario)
            session.commit()
            print "Usuario %s adicionado com sucesso"%nomeUser
        except Exception as e:
            session.rollback()

    def acessar_sistema(self):
        print "Acessando sistema"
        try:
            engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            emailUser = raw_input("Informe seu email: ")
            senhaUser = raw_input("Digite a sua senha de usuario: ")
            while True:
                usuario = session.query(Usuarios).filter(Usuarios.email==emailUser).first()
                if usuario == None:
                    emailUser = raw_input("Usuario nao encontrado. Digite o seu email: ")
                else:
                    break
            userPass = session.query(Usuarios).filter(Usuarios.email==emailUser, Usuarios.senha==senhaUser).first()
            count = 1
            while count <=4:
                if userPass == None:
                    senhaUser = raw_input("senha incorreta. Digite a senha novamente ou s para \"esqueci a senha\" (tentativa %s de 3): "%count)
                    userPass = session.query(Usuarios).filter(Usuarios.email==emailUser, Usuarios.senha==senhaUser).first()
                    count += 1

                    if senhaUser == 's':
                        secretQuestion = raw_input("Quem e o seu maior fa? ")
                        if secretQuestion == 'arnold':
                            printPass = session.query(Usuarios).filter(Usuarios.email==emailUser).first()
                            print "Sua senha e",printPass.senha
                        else:
                            print "Resposta incorreta. Saindo do sistema"
                            sys.exit()

                else:
                    print "Usuario autenticado"
                    break

        except Exception as e:
            print "Erro: %s"%e
            session.rollback()


    def alterar_senha(self):
        print "Alteracao de senha"
        try: 
            engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            while True:
                emailUser = raw_input("Digite o seu email: ")
                senhaUser = raw_input("Digite a sua senha atual: ")
                usuario = session.query(Usuarios).filter(Usuarios.email==emailUser,Usuarios.senha==senhaUser).first()
                if usuario == None:
                    print "Usuario ou senha incorretos"
                else:
                    break

            while True:
                newSenha = raw_input("Digite a sua nova senha: ")
                confirmNew = raw_input("Confirme a sua nova senha: ")
                if confirmNew != newSenha:
                    print "As senhas nao coincidem"
                else:
                    usuario.senha = newSenha
                    print "Senha alterada com sucesso"
                    session.commit()
                    break
        except Exception as e:
            print "Erro: %s"%e
            session.rollback()

    def listar_adm(self):
        print "Lista de administradores do sistema"
        try:
            engine = create_engine("postgresql://onxentiadmin:123456@127.0.0.1/test")
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            usuarios = session.query(Usuarios).all()
            for u in usuarios:
                print "Id:",u.id,"Nome:",u.nome,"E-mail:",u.email
        except Exception as e:
            print "Erro: %s"%e

    def sair(self):
        print "Saindo do sistema"
        sys.exit()
