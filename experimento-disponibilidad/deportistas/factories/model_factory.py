from faker import Faker
from faker_sqlalchemy import SqlAlchemyProvider

from models.database import db


class ModelFactory:
    cls = None
    custom_factory = None

    def __init__(self, cls, custom_factory=None):
        self.cls = cls
        self.custom_factory = custom_factory

    def factory(self):
        fake = Faker()
        fake.add_provider(SqlAlchemyProvider)

        return fake.sqlalchemy_model(self.cls)

    def create(self, count: int = 1):
        for _ in range(count):
            if self.custom_factory:
                db.session.add(self.custom_factory())
            else:
                db.session.add(self.factory())
        db.session.commit()
