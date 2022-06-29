from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

supermercado_api = Blueprint("supermercado_api", __name__)
# from app.produto.model import Produto


class Supermercado(BaseModel):
    __tablename__ = "supermercado"

    id = db.Column(db.Integer, primary_key=True)

    # Atributos próprios
    nome = db.Column(db.String(100))
    endereco = db.Column(db.String(100))
    telefone = db.Column(db.Column(db.String(11)))
    horario_de_funcionamento = db.Column(db.String(5))
    dias_de_funcionamento = db.Column(db.String(100))

    # Relacionamentos
    
    # Relação de 1 para muitos  
    clientes = db.relationship("Cliente", backref='supermercado')
    entregadores = db.relationship("Entregador", backref='supermercado')
    produtos = db.relationship("Produto", backref='supermercado')
    suportes = db.relationship("Suporte", backref='supermercado')
    


