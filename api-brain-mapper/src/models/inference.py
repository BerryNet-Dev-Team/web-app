from ..database.dbConnection import db

class Inference(db.Model):
    __tablename__ = 'inferences'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(60), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    images = db.Column(db.ARRAY(db.String), nullable=False)
    maps = db.Column(db.ARRAY(db.String), nullable=False)
    generatedImages = db.Column(db.ARRAY(db.String), nullable=True)
    createdOn = db.Column(db.DateTime(), nullable=False)
    completedOn = db.Column(db.DateTime(), nullable=True)
