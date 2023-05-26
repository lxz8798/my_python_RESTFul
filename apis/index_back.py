from flask import Blueprint
from flask_restx import Api, Namespace, Resource

index_api = Blueprint('index', __name__)
api = Api(index_api, title='Index API', version='1.0', doc='/docs')

index_ns = Namespace('index', description='Index API')


@api.route('')
class IndexResource(Resource):
    def get(self):
        return {'message': 'GET /v1/index'}

    def post(self):
        return {'message': 'POST /v1/index'}

    def put(self):
        return {'message': 'PUT /v1/index'}

    def delete(self):
        return {'message': 'DELETE /v1/index'}


api.add_namespace(index_ns)
