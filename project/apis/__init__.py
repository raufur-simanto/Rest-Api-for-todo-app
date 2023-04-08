from flask_restx import Api
from project.apis.api import table_namespace
# from flask import current_app as app

# api docs
api = Api(version="2.0", title="Crud Api", doc='/docs')
# app.logger.info(api)
api.add_namespace(table_namespace, path='/api/todo')