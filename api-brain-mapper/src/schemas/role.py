from ..models.role import Role
from ..database.serializers_utils import ma

class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        exclude = ["users"]

role_schema = RoleSchema()