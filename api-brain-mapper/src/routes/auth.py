import os
import json
from flask import Blueprint, request, redirect, jsonify, abort, g
from werkzeug.exceptions import HTTPException
from sqlalchemy import select
from ..models.user import User
from ..schemas.user import user_schema
from ..database.dbConnection import db

from ..security.jwt_utils import encode_auth_jwt
from ..security.decorators_utils import auth_required
from ..security.crypto_utils import hashPassword

# Open file with available roles
rolesFile = os.path.join(os.getcwd(), "src/database/reference-data/ROLES.json")
with open(rolesFile) as f:
  availableRoles = json.load(f)

# Setup blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/addUser', methods=['POST'])
@auth_required(["ADMIN"])
def addUser():
    try:
        req = request.json

        # Check if request has enough properties needed
        required_keys = ['name', 'lastName', 'email', 'passwd', 'role']
        if not all(key in req for key in required_keys):
            abort(400, 'BAD REQUEST')

        # Get request properties
        name = req['name']
        lastName = req['lastName']
        email = req['email']
        password = req['passwd']
        role = req['role']

        if(role not in availableRoles):
            abort(400, 'BAD REQUEST')

        # Search for existent user with same email
        stmt = select(User).where(User.email == email)
        result = db.session.execute(statement=stmt)

        userExists = result.fetchone() is not None

        if(userExists):
            abort(400, 'BAD REQUEST')

        # Add new user to DB
        new_user = User(
            name=name,
            lastName=lastName,
            email=email,
            password=hashPassword(password),
            role=role
        )

        db.session.add(new_user)
        db.session.commit()

        # Return response
        return jsonify({"message": "user added successfully"})

    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, e.description)
        else:
            print(e)
            abort(500)


@auth.route('/login', methods=['POST'])
def login():
    try:
        req = request.json

        # Check if request has enough properties needed
        required_keys = ['email', 'passwd']
        if not all(key in req for key in required_keys):
            abort(400, 'BAD REQUEST')

        # Get request properties
        email = req['email']
        password = req['passwd']
        
        # Check if user exists
        stmt = select(User).where(
            User.email == email,
            User.password == hashPassword(password)
        )
        result = db.session.execute(statement=stmt)

        user = result.scalar_one_or_none()

        # If no user matched email and password in req, return error
        if(user is None):
            abort(400, 'BAD REQUEST')

        # Serialize into JSON the DB response Obj (also exclude unwanted info)
        user_serialized = user_schema.dump(user)

        #Create jwt
        auth_jwt = encode_auth_jwt(user.id)

        # Generate and return response
        responseData = {
            'loggedIn': True,
            'user': user_serialized
        }

        return jsonify(responseData), 200, {"Authorization": f"Bearer {auth_jwt}"}
    except Exception as e:
        if isinstance(e, HTTPException):
            abort(e.code, e.description)
        else:
            abort(500)

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
        if isinstance(e, HTTPException):
            abort(e.code, e.description)
        else:
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

