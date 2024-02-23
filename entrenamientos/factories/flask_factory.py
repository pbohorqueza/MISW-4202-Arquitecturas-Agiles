import os

from dotenv import load_dotenv
from flask import Flask
from celery.schedules import crontab

from models.database import db
from .celery_factory import celery_init_app

load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app_context = app.app_context()
    app_context.push()

    app.config.from_mapping(
        CELERY=dict(
            broker_url=os.environ.get("QUEUE_URL"),
            result_backend=os.environ.get("QUEUE_URL"),
            task_ignore_result=True,
            beat_schedule={
                'beat': {
                    'task': 'jobs.tasks.beat',
                    'schedule': 5,
                }
            }
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)
    db.init_app(app)
    db.create_all()
    return app
