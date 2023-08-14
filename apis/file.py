from flask_restx import Namespace, Resource
from base.api_route import route
from flask import request

file_ns = Namespace('file', description='Home operations')

@file_ns.route('/')
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

@file_ns.route('/upload')
class FileUpload(Resource):
    @route('')
    def get(self):
        return {'message': 'GET /v1/file/upload'}

    def post(self):
        uploaded_file = request.files['file']
        return {'message': 'POST /v1/file/upload'}