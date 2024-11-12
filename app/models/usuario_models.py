from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from config.database import db

Base = declarative_base()


class Usuario(Base):
    # Definindo características da tabela no banco de dados.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(250))
    email = Column(String(250), unique=False)
    senha = Column(String(250))
    cpf = Column(String(14), unique=True)


    # Definindo atributos da classe
    def __init__(self, nome: str, email: str, senha: str, cpf: str):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf


# Criando tabela no banco de dados
Base.metadata.create_all(bind=db)