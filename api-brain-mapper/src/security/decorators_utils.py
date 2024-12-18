from functools import wraps
from flask import request, abort, g
from werkzeug.exceptions import HTTPException
from sqlalchemy import select
from ..security.jwt_utils import decode_auth_jwt
from ..models.user import User
from ..schemas.user import user_schema
from ..database.dbConnection import db

def auth_required(requiredRoles=None):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if (auth_header):
                auth_jwt = auth_header.split(" ")[1]
            else:
                auth_jwt = ""

            uid = None
            try:
                if len(auth_jwt) > 0:
                    uid = decode_auth_jwt(auth_jwt)
                else:
                    abort(400, 'No token provided')
            except Exception as e:
                if isinstance(e, HTTPException):
                    abort(e.code, e.description)
                else:
                    abort(401, 'Invalid/Expired token')
            
            # If reached this point, means uid has something so lets search user
            # Check if user exists
            stmt = select(User).where(User.id == uid)
            result = db.session.execute(statement=stmt)

            # If no user found, return error
            user = result.scalar_one_or_none()
            if(user is None):
                abort(400, 'BAD REQUEST')

            # Store the uid and role in g so it's accessible throughout the request
            g.uid = uid
            g.role = user.role.name

            # If user role is not in the requiredRoles return error
            if(requiredRoles is not None):
                if(user.role.name not in requiredRoles):
                    abort(403, 'Forbidden: You do not have the required role')

            return f(*args, **kwargs)

        return decorated
    return decorator
