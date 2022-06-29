from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

entrega_api = Blueprint("entrega_api", __name__)


class Entrega(BaseModel):
    __tablename__ = "entrega"

    id = db.Column(db.Integer, primary_key=True)
    
    # Atributos próprios
    bairro = db.Column(db.String(100))
    rua = db.Column(db.String(100))
    numero = db.Column(db.String(5))
    complemento = db.Column(db.String(100))
    ponto_de_referencia = db.Column(db.String(100))
    hora_da_entrega = db.Column(db.String(5))
    data_da_entrega = db.Column(db.String(10))

    # Relacionametos
    
    # muito para muito
    entregadores = db.relationship("Entregador", secondary="entregador_entrega", backref="entrega_dos_entregadores")
    
    # 1 para 1
    clientes = db.Column(db.Integer, db.ForeignKey("cliente.id"))

    # 1 para muitos
    produtos = db.Column(db.Integer, db.ForeignKey("produto.id"))

class EntregadorEntrega(BaseModel):
    __tablename__ = "entregador_entrega"

    id = db.Column(db.Integer, primary_key=True)

    entregadores = db.Column(db.Integer, db.ForeignKey("entregador.id"))
    entrega_mercado = db.Column(db.Integer, db.ForeignKey("entrega.id"))