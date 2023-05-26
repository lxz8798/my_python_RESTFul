from flask_swagger_ui import get_swaggerui_blueprint
from base.JSONEncoder import JSONEncoder

from flask import Flask

app = Flask(__name__)

app.json_encoder = JSONEncoder

SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'My Flask REST API'
    }
)