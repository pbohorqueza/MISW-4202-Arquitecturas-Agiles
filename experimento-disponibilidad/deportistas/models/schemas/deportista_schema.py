import requests
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from config import ENTRENAMIENTOS_URL
from enums.genero import Genero
from ..deportista import Deportista


class DeportistaSchema(SQLAlchemyAutoSchema):
    genero = fields.Enum(Genero, by_value=True, allow_none=True)
    entrenamientos = fields.Method('get_entrenamientos')

    class Meta:
        model = Deportista
        load_instance = True

    def get_entrenamientos(self, obj):
        if 'load_entrenamientos' in self.context and self.context['load_entrenamientos']:
            response = requests.get(ENTRENAMIENTOS_URL + f"/deportistas/{obj.id}/entrenamientos")

            if response.status_code == 200:
                return response.json()
            else:
                return []
        else:
            return []
