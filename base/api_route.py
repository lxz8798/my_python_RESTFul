from flask import jsonify
from functools import wraps
from base.APIResponse import APIResponse

def route(*args, **kwargs):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            res = APIResponse(result)
            return jsonify(res.body())
        return wrapper
    return decorator
