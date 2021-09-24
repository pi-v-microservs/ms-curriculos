from data.database import db


class Formacao(db.Model):
    __tablename__ = 'formacao'
    id_formacao = db.Column('id_formacao', db.Integer, primary_key=True)
    nome_formacao = db.Column('nome_formacao', db.Integer, primary_key=True)
    nivel = db.Column('nivel', db.VARCHAR)
    instituicao = db.Column('instituicao', db.VARCHAR)
    descricao = db.Column('descricao', db.TEXT)
    data_inicio = db.Column('data_inicio', db.Date)
    data_fim = db.Column('data_fim', db.Date)
    id_curriculo = db.Column(db.Integer, db.ForeignKey('curriculos.id_curriculo'))

    def to_dict(self):
        return {key: val for key, val in self.__dict__.items()
                if not key.startswith('_')}
