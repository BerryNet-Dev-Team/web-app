from ..models.user import User
from ..schemas.request import request_schema
from ..database.serializers_utils import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ["password"]
    
    # Setup a nested schema to serialize requests
    requests = ma.Nested(request_schema, many=True)

user_schema = UserSchema()