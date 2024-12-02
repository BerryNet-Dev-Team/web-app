from ..database.dbConnection import db
from ..models.inference import Inference
from ..models.scene import Scene

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    inferences = db.relationship("Inference", backref="users")
    scenes = db.relationship("Scene", backref="users")
