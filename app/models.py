from app import db
from datetime import datetime
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable =True)
    tarefas = db.relationship('Tarefa', backref='usuario', lazy=True)

class Tarefa(db.Model, UserMixin):
    id_tarefa = db.Column(db.Integer, primary_key=True)
    desc_tarefa = db.Column(db.String, nullable=True)
    nome_setor = db.Column(db.String, nullable =True)
    prioridade = db.Column(db.String, nullable =True)
    data_cadastro = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String, nullable =True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    
    