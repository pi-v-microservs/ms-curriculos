import datetime

from flask import Blueprint, request

from data.database import db
from domain.models.Curriculo import Curriculo
from domain.models.ExperienciaProfissional import ExperienciaProfissional
from domain.models.Formacao import Formacao

bp = Blueprint('experiencias_profissionais_controllers', __name__, url_prefix='/experiencias_profissionais')


@bp.route('/list', methods=['GET'])
def list_experiencias_profissionais_curriculo():
    try:
        return {'experiencias_profissionais': [
            experiencia.to_dict() for experiencia in (ExperienciaProfissional
                                                      .query
                                                      .filter_by(id_candidato=request.args.get('id_curriculo'))
                                                      .all())]}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/get', methods=['GET'])
def get_experiencia_profissional():
    try:
        return (ExperienciaProfissional
                .query
                .filter_by(id_curriculo=request.args.get('id_experiencia_profissional'))
                .first()
                .to_dict())
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/create', methods=['POST'])
def create_experiencia_profissional():
    try:
        experiencia_criar = ExperienciaProfissional(**request.form)
        db.session.add(experiencia_criar)
        db.session.commit()
        return {'message': 'experiencia profissional criada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/update', methods=['PUT'])
def update_experiencia_profissional():
    try:
        experiencia_atualizar = (ExperienciaProfissional
                                 .query
                                 .filter_by(id_curriculo=request.form.get('id_experiencia_profissional'))
                                 .first())

        experiencia_atualizar.nome_empresa = request.form.get('nome_empresa')
        experiencia_atualizar.cargo = request.form.get('cargo')
        experiencia_atualizar.descricao = request.form.get('descricao')
        experiencia_atualizar.data_inicio = request.form.get('data_inicio')
        experiencia_atualizar.data_fim = request.form.get('data_fim')

        db.session.commit()
        return {'message': 'experiencia profissional atualizada com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}


@bp.route('/delete', methods=['DELETE'])
def delete_experiencia_profissional():
    try:
        curriculo_deletar = Formacao.query.filter_by(id_formacao=request.form.get('id_formacao')).first()

        db.session.delete(curriculo_deletar)
        db.session.commit()
        return {'message': 'curriculo deletado com sucesso'}
    except Exception as exc:
        return {'error': str(exc)}
