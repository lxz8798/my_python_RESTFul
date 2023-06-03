from flask import Blueprint
from flask_restx import Api

from apis.home import home_ns
from apis.file import file_ns

v1_bp = Blueprint('v1', __name__, url_prefix='/v1')

v1_api = Api(v1_bp)

v1_api.add_namespace(file_ns)
v1_api.add_namespace(home_ns)
