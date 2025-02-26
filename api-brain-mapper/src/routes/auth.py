import os
import json
from flask import Blueprint, request, redirect, jsonify, abort, g
from werkzeug.exceptions import HTTPException
from logs.logger import logger

from sqlalchemy import select
from ..models.user import User
from ..schemas.user import user_schema
from ..database.dbConnection import db

from ..security.jwt_utils import *
from ..security.decorators_utils import auth_required
from ..security.crypto_utils import *

# Open file with available roles
rolesFile = os.path.join(os.getcwd(), "src/database/reference-data/ROLES.json")
with open(rolesFile) as f:
  availableRoles = json.load(f)

# Setup blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/addUser', methods=['POST'])
@auth_required(["ADMIN"])
def addUser():
    req = request.json

    # Check if request has enough properties needed
    required_keys = ['name', 'lastName', 'email', 'passwd', 'roleId']
    if not all(key in req for key in required_keys):
        abort(400, 'BAD REQUEST')

    # Get request properties
    name = req['name']
    lastName = req['lastName']
    email = req['email']
    password = req['passwd']
    roleId = req['roleId']

    # Search for existent user with same email
    try:
        stmt = select(User).where(User.email == email)
        result = db.session.execute(statement=stmt)
    except Exception as exc:
        logger.exception('Error fetching from DB')
        abort(500, 'INTERNAL ERROR')

    userExists = result.fetchone() is not None
    if(userExists):
        abort(400, 'BAD REQUEST')

    # Check password length, limited to 50 due to mitigate 70+ chars error with hash
    if len(password) > 50:
        abort(400, 'passwd_length')

    # Add new user to DB
    new_user = User(
        name=name,
        lastName=lastName,
        email=email,
        password=hashPassword(password),
        roleId=roleId
    )

    # Add user to DB
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as exc:
        logger.exception('Error saving user in DB')
        abort(500, 'Error saving new user')

    # Return response
    return jsonify({"message": "user added successfully"})


@auth.route('/login', methods=['POST'])
def login():
    req = request.json

    # Check if request has enough properties needed
    required_keys = ['email', 'passwd']
    if not all(key in req for key in required_keys):
        abort(400, 'BAD REQUEST')

    # Get request properties
    email = req['email']
    password = req['passwd']

    try:
        # Query to search user by email
        stmt = select(User).where(
            User.email == email
        )
        result = db.session.execute(statement=stmt)
    except Exception as exc:
        logger.exception('Error fetching from DB')
        abort(500, 'INTERNAL ERROR')

    # If no user matched the email in req, return error
    user = result.scalar_one_or_none()
    if(user is None):
        abort(400, 'BAD REQUEST')

    # If password not match, return error
    if (not checkPasswordHash(user.password, password)):
        abort(401, 'wrong_password')

    # Serialize into JSON the DB response Obj (also exclude unwanted info)
    user_serialized = user_schema.dump(user)

    #Create jwt
    try:
        auth_jwt = encode_auth_jwt(user.id)
    except Exception as exc:
        logger.exception('Error generating JWT')
        abort(500, 'INTERNAL ERROR')

    # Generate and return response
    responseData = {
        'loggedIn': True,
        'user': user_serialized
    }

    return jsonify(responseData), 200, {"Authorization": f"Bearer {auth_jwt}"}


@auth.route('/isLoggedIn', methods=['GET'])
def isLoggedIn():
    auth_header = request.headers.get('Authorization')
    if (auth_header):
        auth_jwt = auth_header.split(" ")[1]
    else:
        abort(401, 'UNAUTHORIZED')

    # By default set user as logged in, if something fails change to false
    isLoggedIn = True
    try:
        uid = decode_auth_jwt(auth_jwt)
    except Exception as exc:
        isLoggedIn = False
        if str(exc) == 'invalid_token':
            logger.warning('Possible attack: Trying to hijack session')

    # Generate and return response
    responseData = {
        'loggedIn': isLoggedIn,
    }
    return jsonify(responseData), 200

@auth.route('/getUserRole', methods=['GET'])
@auth_required()
def getRole():
    responseData = {
        "role": g.role
    }
    return jsonify(responseData), 200

@auth.route('/logout', methods=['POST'])
def logout():
    try:
        # Generate and return response
        responseData = {
            'loggedIn': False,
        }

        # This response deletes the JWT from the header, and make next requests fails
        return jsonify(responseData), 200
    except Exception as e:
        logger.error('Error while logging out')
        abort(500)

@auth.route('/protected', methods=['GET'])
@auth_required(["ADMIN"])
def protected():
    try:
        return jsonify({'message': 'Funciona'})
    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, e.description)
        else:
            abort(500)

