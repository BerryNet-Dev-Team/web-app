from ..database.dbConnection import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password