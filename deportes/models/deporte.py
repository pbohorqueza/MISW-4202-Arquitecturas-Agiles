from faker import Faker

from factories import ModelFactory
from .database import db


class Deporte(db.Model):
    __tablename__ = 'deportes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    descripcion = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @classmethod
    def factory(cls):
        def maker():
            faker = Faker()

            return Deporte(
                nombre=faker.name(),
                descripcion=faker.text()
            )

        return ModelFactory(cls, maker)
