from http.client import PRECONDITION_FAILED
from lib2to3.pytree import Base
from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

produto_api = Blueprint("produto_api", __name__)


class Produto(BaseModel):
    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True)
    
    # Atributos próprios
    nome = db.Column(db.String(100))
    cdg_de_barras = db.Column(db.String(10))
    preco = db.Column(db.String(10))
    data_de_fabricacao = db.Column(db.String(10))
    data_de_validade = db.Column(db.String(10))

    # Relacionamentos

    '''mercado 
    clientes
    entrega''' 


