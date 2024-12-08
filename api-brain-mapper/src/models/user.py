from ..database.dbConnection import db
from ..models.inference import Inference
from ..models.scene import Scene
from ..models.role import Role

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    roleId = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role = db.relationship("Role", back_populates="users")
    inferences = db.relationship("Inference")
    scenes = db.relationship("Scene")
