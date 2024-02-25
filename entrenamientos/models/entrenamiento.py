from faker import Faker

from factories import ModelFactory
from .database import db


class Entrenamiento(db.Model):
    __tablename__ = 'entrenamientos'
    id = db.Column(db.Integer, primary_key=True)
    id_deportista = db.Column(db.Integer, nullable=False)
    id_deporte = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    @classmethod
    def factory(cls):
        def maker():
            faker = Faker()

            return Entrenamiento(
                id_deportista=1,
                id_deporte=1,
                fecha=faker.date_time_this_year(before_now=True, after_now=False)
            )

        return ModelFactory(cls, maker)
