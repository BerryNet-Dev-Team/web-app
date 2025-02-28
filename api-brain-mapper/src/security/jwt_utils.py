import os
import jwt
from datetime import datetime, timedelta, timezone

def encode_auth_jwt(uid, expires_in=60):
    try:
        payload = {
            'exp': datetime.now(timezone.utc) + timedelta(minutes=expires_in),
            'iat': datetime.now(timezone.utc),
            'uid': uid
        }

        return jwt.encode(
            payload,
            os.getenv('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        raise e

def decode_auth_jwt(auth_jwt):
    try:
        payload = jwt.decode(
            auth_jwt,
            os.getenv('SECRET_KEY'),
            algorithms=['HS256']
        )

        return payload['uid']

    except jwt.ExpiredSignatureError:
        raise Exception('expired_token')
    except jwt.InvalidTokenError:
        raise Exception('invalid_token')
