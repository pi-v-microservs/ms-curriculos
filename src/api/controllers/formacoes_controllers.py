from flask import Blueprint, request

from data.database import db
from domain.models.Formacao import Formacao

bp = Blueprint('formacoes_controllers', __name__, url_prefix='/formacoes')


@bp.route('/list', methods=['GET'])
def list_formacoes_curriculo():
    try:
        return {'formacoes': [
            formacao.to_dict() for formacao in (Formacao
                                                .query
                                                .filter_by(id_curriculo=request.args.get('id_curriculo'))
                                                .all())]}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/get', methods=['GET'])
def get_formacao():
    try:
        return (Formacao
                .query
                .filter_by(id_formacao=request.args.get('id_formacao'))
                .first()
                .to_dict())
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/create', methods=['POST'])
def create_formacao():
    try:
        formacao_criar = Formacao(**request.form)
        db.session.add(formacao_criar)
        db.session.commit()
        return {'message': 'formacao criada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/update', methods=['PUT'])
def update_formacao():
    try:
        formacao_atualizar = Formacao.query.filter_by(id_formacao=request.form.get('id_formacao')).first()

        formacao_atualizar.nome_formacao = request.form.get('nome_formacao')
        formacao_atualizar.nivel = request.form.get('nivel')
        formacao_atualizar.instituicao = request.form.get('instituicao')
        formacao_atualizar.descricao = request.form.get('descricao')
        formacao_atualizar.data_inicio = request.form.get('data_inicio')
        formacao_atualizar.data_fim = request.form.get('data_fim')

        db.session.commit()
        return {'message': 'formacao atualizada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/delete', methods=['DELETE'])
def delete_curriculo():
    try:
        curriculo_deletar = Formacao.query.filter_by(id_formacao=request.form.get('id_formacao')).first()

        db.session.delete(curriculo_deletar)
        db.session.commit()
        return {'message': 'formacao deletada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}
