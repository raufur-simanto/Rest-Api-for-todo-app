from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
# from project.config import BaseConfig
db = SQLAlchemy()
migrate = Migrate()

# print(BaseConfig.SQLALCHEMY_DATABASE_URI)
def create_app():
    app = Flask(__name__)
    app.config.from_object('project.config.BaseConfig')
    # app.json_encoder = CustomJSONEncoder

    db.init_app(app)
    migrate.init_app(app, db)

    # configure logger
    app.logger.setLevel(logging.INFO)

    # configure api with app
    from project.apis import api
    api.init_app(app)

    ## for flask shell
    @app.shell_context_processor
    def make_shell():
        return {'db': db, 'app': app}

    return app
