from typing import Optional

from data.database import db


class Formacao(db.Model):
    __tablename__ = 'formacao'
    id_formacao = db.Column('id_formacao', db.Integer, primary_key=True)
    id_curriculo = db.Column(db.Integer, db.ForeignKey('curriculos.id_curriculo'))

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()
                if not key.startswith('_')}
