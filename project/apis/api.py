from flask_restx import Namespace, Resource, fields
from project.models import Todo_table
from project import db
from flask import request, current_app as app, json

table_namespace = Namespace("todo")

add_data_input_model = table_namespace.model('add_data_input_model',
            {
                "id": fields.Integer(required=True, description='id'),
                "name": fields.String(required=True, description='name')
            })

data_output_model_nest = table_namespace.model('data_output_model_nest',
                        {
                            "data": fields.Raw(fields.Nested('add_data_input_model')),
                            'message': fields.String(required=True)
                        })


class Add(Resource):
    @table_namespace.expect(add_data_input_model, validate=True)
    @table_namespace.response(400, "Bad Request")
    @table_namespace.response(200, "data added successfully")
    def post(self):
        data = request.get_json()
        app.logger.info(data)

        try:
            todo = Todo_table(id=data.get('id'), name=data.get('name'))
            db.session.add(todo)
            db.session.commit()
        except Exception as e:
            table_namespace.abort(400, "Bad request")
        finally:
            response_obj = {
                'message': "data added successfully",
                'status': 'success'
            }
        return response_obj, 200
    
    
class ShowData(Resource):
    @table_namespace.marshal_with(data_output_model_nest)
    @table_namespace.response(200, "data retrieved successfully")
    @table_namespace.response(400, "Internal server error")
    def get(self):
        try:
            data = Todo_table.query.all()
            response_data = []
            for row in data:
                response_data.append({
                    'id': row.id,
                    'name': row.name
                })
                # app.logger.info(type(response_data))

            # app.logger.info(type(response_data))

            response_obj = {
                'data': response_data, 
                'message': "data retrieved successfully"
            }
            return response_obj, 200
        except Exception as e:
            table_namespace.abort(400, "Internal server error")


class GetDataByName(Resource):
    @table_namespace.marshal_with(add_data_input_model)
    @table_namespace.response(200, "data retrieved successfully")
    @table_namespace.response(500, "Internal server error")
    def post(self):
        try:
            data = request.get_json()
            app.logger.info(data)

            response = Todo_table.query.filter_by(name=data.get('name')).first()
            # app.logger.info(response.id, response.name)
            response_object = {
                'id': response.id,
                'name': response.name
            }

            return response_object, 200
        except Exception as e:
            table_namespace.abort(500, "Internal Server Error")


class RemoveUser(Resource):
    @table_namespace.response(200, "user deleted successfully")
    @table_namespace.response(500, "Internal server error")
    @table_namespace.response(400, "Bad Request")
    def delete(self):
        try:
            data = request.get_json()
            app.logger.info(data)

            user = Todo_table.query.filter_by(name=data.get('name')).first()

            if not user:
                table_namespace.abort(400, "Bad Request")
            
            db.session.delete(user)
            db.session.commit()

            return "user deleted successfully", 200
        except Exception as e:
            table_namespace.abort(500, "Internal server error")


class UpdateInfo(Resource):
    @table_namespace.response(200, "user updated successfully")
    @table_namespace.response(500, "Internal server error")
    @table_namespace.response(400, "Bad Request")
    def put(self):
        try:
            data = request.get_json()
            app.logger.info(data)

            user = Todo_table.query.filter_by(id=data.get('id')).first()

            if not user:
                table_namespace.abort(400, "Bad Request")
            
            user.name = data.get('name')
            db.session.commit()

            return "user updated successfully", 200
        except Exception as e:
            table_namespace.abort(500, "Internal server error")


table_namespace.add_resource(Add, '/add')
table_namespace.add_resource(ShowData, '/get-data')
# table_namespace.add_resource(GetDataByName, '/get-data-name')
# table_namespace.add_resource(RemoveUser, '/delete')
# table_namespace.add_resource(UpdateInfo, '/update')