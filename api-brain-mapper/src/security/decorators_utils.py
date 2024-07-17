from functools import wraps
from flask import request, abort
from werkzeug.exceptions import HTTPException
from ..security.jwt_utils import decode_auth_jwt

def auth_jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if (auth_header):
            auth_jwt = auth_header.split(" ")[1]
        else:
            auth_jwt = ""

        try:
            if len(auth_jwt) > 0:
                decode_auth_jwt(auth_jwt)
            else:
                abort(403, 'No token provided')
        except Exception as e:
            if isinstance(e, HTTPException):
                abort(e.code, e.description)
            else:
                abort(401, 'Invalid/Expired token')

        return f(*args, **kwargs)

    return decorated
