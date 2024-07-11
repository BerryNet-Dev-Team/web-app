from flask import Blueprint, request, redirect, jsonify, abort
from ..models.user import User
from ..database.dbConnection import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/register', methods=['POST'])
def addUser():

    print(request.json)
    name = request.json['name']
    email = request.json['email']

    new_user = User(
        name=name,
        email=email
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "user agregado"})