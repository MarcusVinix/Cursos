from app import db  
from app import manager

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logadouro = db.Column(db.String(100))
    num = db.Column(db.Integer)
    bairro = db.Column(db.String(50))

db.create_all()
manager.create_api(Endereco, methods=['POST', 'DELETE', 'PUT', 'GET'])