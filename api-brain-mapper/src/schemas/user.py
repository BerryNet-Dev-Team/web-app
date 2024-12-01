from ..models.user import User
from .inference import inference_schema
from .scene import scene_schema
from ..database.serializers_utils import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ["password"]
    
    # Setup a nested schema to serialize requests
    requests = ma.Nested(inference_schema, many=True)
    scenes = ma.Nested(scene_schema, many=True)

user_schema = UserSchema()