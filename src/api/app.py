import logging

from flask import Flask
from flask.cli import with_appcontext

from api.config import config
from data.database import db


def create_app(config_opt: str = "default"):
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)
    app.config.from_object(config[config_opt])
    config[config_opt].init_app(app)

    db.init_app(app)

    from api.controllers import curriculos_controllers
    app.register_blueprint(curriculos_controllers.bp)

    from api.controllers import formacoes_controllers
    app.register_blueprint(formacoes_controllers.bp)

    from api.controllers import experiencias_profissionais_controllers
    app.register_blueprint(experiencias_profissionais_controllers.bp)

    @app.cli.command(name='init_db')
    @with_appcontext
    def init_db():
        db.create_all()

    app.cli.add_command(init_db)

    return app
