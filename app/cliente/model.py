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

    nome = db.Column(db.String(100))
    data_de_nascimento = db.Column(db.String(10))
    cpf = db.Column(db.String(11))
    celular = db.Column(db.String(11))
    email = db.Column(db.String(100))
    # Definir a chave estrangeira/relacionamento entre as tabelas
    endereco = db.Column(db.String(200))

    # Relacionamentos
    
    # 1 para muitos
    mercado = db.Column(db.Integer, db.ForeignKey("supermercado.id"))
    
    # muito para muito
    entregadores = db.relationship("Entregador", secondary="entregador_cliente", backref="cliente_dos_entregadores")

    # 1 para 1
    entrega_mercado = db.relationship("Entrega", backref="cliente", uselist=False)
    
    # muito para muito
    #produtos = db.Column()
    
    # 1 para muitos
    suporte_mercado = db.Column(db.Integer, db.ForeignKey("suporte.id"))

# muito para muito
#entregadores 

class EntregadorECliente(BaseModel):
    __tablename__ = "entregador_cliente"

    id = db.Column(db.Integer, primary_key=True)

    entregadores = db.Column(db.Integer, db.ForeignKey("entregador.id"))
    clientes = db.Column(db.Integer, db.ForeignKey("cliente.id"))



