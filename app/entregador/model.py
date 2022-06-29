from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

entregador_api = Blueprint("entregador_api", __name__)


class Entregador(BaseModel):
    __tablename__ = "entregador"

    id = db.Column(db.Integer, primary_key=True)
    
    # Atributos próprios
    nome = db.Column(db.String(100))
    data_de_nascimento = db.Column(db.String(8))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(100))
    celular = db.Column(db.String(11))
    veiculo = db.Column(db.String(10))
    placa_veiculo = db.Column(db.String(10))

    # Relacionamentos
    
    # 1 para muitos
    mercado = db.Column(db.Integer, db.ForeignKey('supermercado.id'))

    # muito para muito
    #cliente = db.relationship("Cliente", backref="entregador")
    
    # muito para muito
    #entrega_mercado = db.relationship("Entrega", backref='entregador')

