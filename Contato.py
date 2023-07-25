from config import db

class Contato(db.Model):
    __tablename__ = "contato"
    ID = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(100))
    sobrenome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(20))