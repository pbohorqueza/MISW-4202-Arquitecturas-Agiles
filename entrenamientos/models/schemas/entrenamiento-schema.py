from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..entrenamiento import Entrenamiento


class EntrenamientoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Entrenamiento
        load_instance = True
