from base import app
from flask_restx import Api
from flask_cors import CORS

from apis.home import home_api

from base import swaggerui_blueprint, SWAGGER_URL

CORS(app)  # 解决跨域问题

api = Api(app)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# 注册蓝图
app.register_blueprint(home_api, url_prefix='/v1/home')

if __name__ == '__main__':
    app.run(debug=True)
