
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
    categoria = db.Column(db.String(100))
    preco = db.Column(db.String(10))
    data_de_fabricacao = db.Column(db.String(10))
    data_de_validade = db.Column(db.String(10))

    # Relacionamentos
    
    # 1 para muitos
    mercado = db.Column(db.Integer, db.ForeignKey('supermercado.id'))

    # muito para muito
    clientes = db.relationship("Cliente", secondary="cliente_produto", backref="produto_dos_clientes")

    # 1 para muito
    entrega_mercado = db.relationship("Entrega", backref="produto")

# Classe de associação
class ClienteEProduto(BaseModel):
    __tablename__ = "cliente_produto"

    id = db.Column(db.Integer, primary_key=True)

    produtos = db.Column(db.Integer, db.ForeignKey("produto.id"))
    clientes = db.Column(db.Integer, db.ForeignKey("cliente.id"))