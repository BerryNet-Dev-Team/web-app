from ..database.dbConnection import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    users = db.relationship("User", lazy="dynamic", back_populates="role")