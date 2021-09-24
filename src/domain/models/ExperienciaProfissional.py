from datetime import datetime
from typing import Optional

from data.database import db


class ExperienciaProfissional(db.Model):
    __tablename__ = 'experiencias_profissionais'
    id_experiencia_profissional = db.Column('id_experiencia_profissional', db.Integer, primary_key=True)
    id_curriculo = db.Column(db.Integer, db.ForeignKey('curriculos.id_curriculo'))

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()
                if not key.startswith('_')}
