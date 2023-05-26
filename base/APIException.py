from werkzeug.exceptions import HTTPException
from flask import json

class APIException(HTTPException):
    code = 500
    msg = 'server error'

    def __init__(self, msg=None, code=None):
        if msg:
            self.msg = msg
        if code:
            self.code = code
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None,scope=None):
        body = {
            'msg': self.msg,
            'code': self.code
        }
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None,scope=None):
        return [('Content-Type', 'application/json')]
