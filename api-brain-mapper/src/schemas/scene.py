from ..models.scene import Scene
from ..database.serializers_utils import ma

class SceneSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Scene

scene_schema = SceneSchema()