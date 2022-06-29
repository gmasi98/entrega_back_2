from app.extensions import db
from app.model import BaseModel


class Suporte(BaseModel):
    __tablename__ = "suporte"
    
    id = db.Column(db.Integer, primary_key=True)

    # Atributos próprios
    telefone = db.Column(db.String(11))
    email = db.Column(db.String(100))

    # Relacionametos
    '''cliente 
    entregador
    supermercado'''