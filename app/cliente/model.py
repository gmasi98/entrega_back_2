from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

cliente_api = Blueprint("cliente_api", __name__)

# Classe Cliente é herdeira da Classe BaseModel
# Relacionamentos são colocados abaixo 
class Cliente(BaseModel):
    __tablename__ = "cliente" 

    # definindo como chave primária/relacionamento - vai estar ligada a que tabela: supermercado ?...
    # A chave primária vai interconectar as tabelas de maneira que vai possuir um mesmo cdg dela em outra tabela para isso
    # Esse id vai servir para identificar o cliente e aí deverá apontar para o outro id presente em outra tabela a qual se relacionou com a tabela cliente
    id = db.Column(db.Integer, primary_key=True)
    
    # Atributos próprios da classe 
    nome = db.Column(db.Strig(100))
    data_de_nascimento = db.Column(db.String(10))
    cpf = db.Column(db.String(11))
    celular = db.Column(db.String(11))
    email = db.Column(db.String(100))
    # Definir a chave estrangeira/relacionamento entre as tabelas
    endereco = db.Column(db.String(200))

    # Relacionamentos
    mercado = db.Column(db.Integer, db.Foreignkey("supermercado.id")) 
    '''entregador 
    entrega 
    produto 
    suporte''' 

