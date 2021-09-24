from datetime import datetime
from typing import List, Optional

from data.database import db
from domain.models.Formacao import Formacao
from domain.models.ExperienciaProfissional import ExperienciaProfissional


class Curriculo(db.Model):
    __tablename__ = 'curriculos'
    id_curriculo = db.Column('id_curriculo', db.Integer, primary_key=True)
    id_candidato = db.Column('id_candidato', db.Integer)
    titulo = db.Column('titulo', db.UnicodeText)
    cargo = db.Column('cargo', db.UnicodeText)
    objetivo = db.Column('objetivo', db.UnicodeText)
    data_criacao = db.Column('data_criacao', db.DATETIME, default=datetime.now())
    data_alteracao = db.Column('data_alteracao', db.DATETIME)

    formacoes: List[Formacao] = db.relationship('Formacao', backref='curriculo')
    experiencias_profissionais: List[ExperienciaProfissional] = db.relationship('ExperienciaProfissional', backref='curriculo')

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()
                if not (key.startswith('_'))}
