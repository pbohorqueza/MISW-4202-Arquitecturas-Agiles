from enums.genero import Genero
from enums.deporte import Deporte
from factories import ModelFactory
from .database import db
from faker import Faker


class Deportista(db.Model):
    __tablename__ = 'deportistas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), nullable=False)
    genero = db.Column(db.Enum(Genero), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    estatura = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @classmethod
    def factory(cls):
        def maker():
            faker = Faker()

            return Deportista(
                nombre=faker.name(),
                genero=faker.random_element(elements=(Genero.MASCULINO, Genero.FEMENINO)),
                edad=faker.random_int(min=18, max=50),
                peso=faker.random_int(min=60, max=100),
                estatura=faker.random_int(min=150, max=200)
            )

        return ModelFactory(cls, maker)
