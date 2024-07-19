from ..models.user import User
from ..database.serializers_utils import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ["password"]

user_schema = UserSchema()