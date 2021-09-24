from datetime import datetime
from typing import Optional

from data.database import db


class ExperienciaProfissional(db.Model):
    __tablename__ = 'experiencias_profissionais'
    id_experiencia_profissional = db.Column('id_experiencia_profissional', db.Integer, primary_key=True)
    nome_empresa = db.Column('nome_empresa', db.VARCHAR)
    cargo = db.Column('cargo', db.VARCHAR)
    descricao = db.Column('descricao', db.TEXT)
    data_inicio = db.Column('data_inicio', db.Date)
    data_fim = db.Column('data_fim', db.Date)
    id_curriculo = db.Column(db.Integer, db.ForeignKey('curriculos.id_curriculo'))

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()
                if not key.startswith('_')}
