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

    # Relacionametos
    
    '''entregador 
    cliente 
    produto''' 
