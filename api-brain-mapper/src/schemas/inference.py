from ..models.inference import Inference
from ..database.serializers_utils import ma

class InferenceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inference

inference_schema = InferenceSchema()