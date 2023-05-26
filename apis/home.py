from flask import Blueprint
from flask_restx import Api, Namespace, Resource
from base.api_route import route

from base.APIException import APIException

import time
import decimal
import datetime

home_api = Blueprint('home', __name__)
api = Api(home_api)

# 创建 home 蓝图并设置命名空间
home_ns = api.namespace('home', description='Home operations')

@home_ns.route('')
class HomeResource(Resource):
    @route(home_api, '')
    def get(self):
        result = {
            'msg': 'GET /v1/home',
            'time': time.strftime('%Y-%m-%d %H:%M:%S'),
            'time2': datetime.datetime.now(),
            'decimal': decimal.Decimal('2.3838'),
        }
        return result

    def post(self):
        return {'message': 'POST /v1/home'}

    def put(self):
        return {'message': 'PUT /v1/home'}

    def delete(self):
        return {'message': 'DELETE /v1/home'}

api.add_namespace(home_ns)
