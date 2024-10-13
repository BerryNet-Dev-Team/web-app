from ..database.dbConnection import db

class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(60), nullable=False)
    originalScansUrls = db.Column(db.ARRAY(db.String), nullable=False)
    segmentationResultsUrls = db.Column(db.ARRAY(db.String), nullable=True)
    generatedImagesUrls = db.Column(db.ARRAY(db.String), nullable=True)
    createdOn = db.Column(db.DateTime(), nullable=False)
    completedOn = db.Column(db.DateTime(), nullable=True)
