from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import requests
from config import DEPORTISTAS_URL, DEPORTES_URL

from ..entrenamiento import Entrenamiento


class EntrenamientoSchema(SQLAlchemyAutoSchema):
    deportista = fields.Method('get_deportista')
    deporte = fields.Method('get_deporte')

    class Meta:
        model = Entrenamiento
        load_instance = True

    def get_deportista(self, obj):
        if 'load_deportista' in self.context and self.context['load_deportista']:
            response = requests.get(DEPORTISTAS_URL + f"/{obj.id_deportista}")

            if response.status_code == 200:
                return response.json()
            else:
                return None
        else:
            return None

    def get_deporte(self, obj):
        if 'load_deporte' in self.context and self.context['load_deporte']:
            response = requests.get(DEPORTES_URL + f"/{obj.id_deporte}")

            if response.status_code == 200:
                return response.json()
            else:
                return None
        else:
            return None
