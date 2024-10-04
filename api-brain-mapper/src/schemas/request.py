from ..models.request import Request
from ..database.serializers_utils import ma

class RequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Request

request_schema = RequestSchema()