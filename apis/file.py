from flask_restx import Namespace, Resource
from base.api_route import route

file_ns = Namespace('file', description='Home operations')

@file_ns.route('/v1/file')
class HomeResource(Resource):
    @route('')
    def get(self):
        result = {
            'msg': 'GET /v1/file',
        }
        return result

    def post(self):
        return {'message': 'POST /v1/file'}

    def put(self):
        return {'message': 'PUT /v1/file'}

    def delete(self):
        return {'message': 'DELETE /v1/file'}

