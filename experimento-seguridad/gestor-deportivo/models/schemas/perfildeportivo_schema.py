import requests
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..perfildeportivo import PerfilDeportivo


class PerfilDeportivoSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = PerfilDeportivo
        load_instance = True

    
