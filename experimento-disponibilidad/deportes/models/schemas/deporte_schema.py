from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..deporte import Deporte


class DeporteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Deporte
        load_instance = True
