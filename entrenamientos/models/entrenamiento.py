from .database import db
from faker import Faker
from faker_sqlalchemy import SqlAlchemyProvider


class Entrenamiento(db.Model):
    __tablename__ = 'entrenamientos'
    id = db.Column(db.Integer, primary_key=True)
    deportista_id = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def factory():
        fake = Faker()
        fake.add_provider(SqlAlchemyProvider)

        return fake.sqlalchemy_model(Entrenamiento)
