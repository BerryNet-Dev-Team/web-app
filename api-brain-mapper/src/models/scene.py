from ..database.dbConnection import db

class Scene(db.Model):
    __tablename__ = 'scenes'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(200), nullable=False)
    images = db.Column(db.ARRAY(db.String), nullable=False)
    maps = db.Column(db.ARRAY(db.String), nullable=False)
    uploadedOn = db.Column(db.DateTime(), nullable=False)
