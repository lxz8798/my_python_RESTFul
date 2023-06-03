from flask_cors import CORS
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

from apis.v1 import v1_bp
app.register_blueprint(v1_bp, url_prefix='/v1')

SWAGGER_URL = '/swagger'
API_URL = '/v1/swagger.json'

swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask Swagger UI"
    }
)

app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

CORS(app)  # 解决跨域问题

if __name__ == '__main__':
    app.run(debug=True)