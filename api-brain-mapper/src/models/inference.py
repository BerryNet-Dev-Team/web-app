from ..database.dbConnection import db

class Inference(db.Model):
    __tablename__ = 'inferences'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    baseImageUrl = db.Column(db.String, nullable=False)
    generatedImageUrl = db.Column(db.String, nullable=True)
    createdOn = db.Column(db.DateTime(), nullable=False)
