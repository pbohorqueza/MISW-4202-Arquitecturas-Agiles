from celery import shared_task

from models.database import db
from models.entrenamiento import Entrenamiento


@shared_task(ignore_result=True)
def beat():
    print('beat')


@shared_task(ignore_result=False)
def create_user():
    db.session.add(Entrenamiento.factory())
    db.session.commit()
