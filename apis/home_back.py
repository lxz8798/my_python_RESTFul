from flask import Blueprint
from flask_restx import Api, Namespace, Resource

home_api = Blueprint('home', __name__)
api = Api(home_api, title='Home API', version='1.0', doc='/docs')

home_ns = Namespace('home', description='Home API')

@api.route('')
class HomeResource(Resource):
    @api.doc(description='Get home data')
    def get(self):
        return {'message': 'GET /v1/home'}

    @api.doc(description='Create home data')
    def post(self):
        return {'message': 'POST /v1/home'}

    @api.doc(description='Update home data')
    def put(self):
        return {'message': 'PUT /v1/home'}

    @api.doc(description='Delete home data')
    def delete(self):
        return {'message': 'DELETE /v1/home'}

api.add_namespace(home_ns)
