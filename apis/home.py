from flask_restx import Namespace, Resource
from base.api_route import route

home_ns = Namespace('home', description='Home operations')

@home_ns.route('')
class HomeResource(Resource):
    @route('')
    def get(self):
        result = {
            'msg': 'GET /v1/home',
        }
        return result

    def post(self):
        return {'message': 'POST /v1/home'}

    def put(self):
        return {'message': 'PUT /v1/home'}

    def delete(self):
        return {'message': 'DELETE /v1/home'}

