from factories import ModelFactory
from .database import db
from faker import Faker
from sqlalchemy import func



class PerfilDeportivo(db.Model):
    __tablename__ = 'perfildeportivo'
    id = db.Column(db.Integer, primary_key=True)
    id_deportista = db.Column(db.Integer, nullable=False)
    incapacidades = db.Column(db.String(256), default="")
    lesiones = db.Column(db.String(256), default="")
    historia_medica = db.Column(db.String(1024), default="")
    created_at = db.Column(db.DateTime, default=func.current_timestamp())

    @classmethod
    def factory(cls):
        def maker():
            faker = Faker()

            return PerfilDeportivo(
                id_deportista=faker.random_int(min=1, max=1000),
                incapacidades=faker.sentence(),
                lesiones=faker.sentence(),
                historia_medica=faker.paragraph()
            )

        return ModelFactory(cls, maker)
