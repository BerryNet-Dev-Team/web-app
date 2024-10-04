from ..database.dbConnection import db

class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    originalScansUrls = db.Column(db.ARRAY(db.String), nullable=False)
    segmentationResultsUrls = db.Column(db.ARRAY(db.String), nullable=False)
    generatedImagesUrls = db.Column(db.ARRAY(db.String), nullable=True)
    createdOn = db.Column(db.Date(), nullable=False)
    completedOn = db.Column(db.Date(), nullable=False)
