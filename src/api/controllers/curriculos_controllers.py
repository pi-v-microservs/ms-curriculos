import datetime

from flask import Blueprint, request

from data.database import db
from domain.models.Curriculo import Curriculo

bp = Blueprint('curriculos_controllers', __name__, url_prefix='/curriculos')


@bp.route('/list', methods=['GET'])
def list_curriculos_candidato():
    try:
        return {'curriculos': [curriculo.to_dict() for curriculo in
                Curriculo.query.filter_by(id_candidato=request.args.get('id_candidato')).all()]}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/get', methods=['GET'])
def get_curriculo():
    try:
        return Curriculo.query.filter_by(id_curriculo=request.args.get('id_curriculo')).first().to_dict()
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/create', methods=['POST'])
def create_curriculo():
    try:
        curriculo_criar = Curriculo(**request.form)
        db.session.add(curriculo_criar)
        db.session.commit()
        return {'message': 'curriculo criado com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/update', methods=['PUT'])
def update_curriculo():
    try:
        curriculo_atualizar = Curriculo.query.filter_by(id_curriculo=request.form.get('id_curriculo')).first()

        curriculo_atualizar.titulo = request.form.get('titulo')
        curriculo_atualizar.cargo = request.form.get('cargo')
        curriculo_atualizar.objetivo = request.form.get('objetivo')

        curriculo_atualizar.data_alteracao = datetime.datetime.now()
        db.session.commit()
        return {'message': 'curriculo atualizado com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/delete', methods=['DELETE'])
def delete_curriculo():
    try:
        curriculo_deletar = Curriculo.query.filter_by(id_curriculo=request.form.get('id_curriculo')).first()

        db.session.delete(curriculo_deletar)
        db.session.commit()
        return {'message': 'curriculo deletado com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}