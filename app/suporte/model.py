from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

suporte_api = Blueprint("suporte_api", __name__)


class Suporte(BaseModel):
    __tablename__ = "suporte"
    
    id = db.Column(db.Integer, primary_key=True)

    # Atributos próprios
    telefone = db.Column(db.String(11))
    email = db.Column(db.String(100))
    nome_do_atendente = db.Column(db.String(100))
    hora_do_atendimento = db.Column(db.String(5))
    data_do_atendimento = db.Column(db.String(10))
    protocolo_de_atendimento = db.Column(db.String(100))

    # Relacionametos
    
    # Relação de 1 para muitos
    mercado = db.Column(db.Integer, db.ForeignKey("supermercado.id"))
    clientes = db.relationship("Cliente", backref="suporte")
    entregadores = db.relationship("Entregador", backref="suporte")