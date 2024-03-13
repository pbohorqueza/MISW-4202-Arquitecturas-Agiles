from flask import Flask

from models.database import db
from .celery_factory import celery_init_app
from config import DATABASE_URL, QUEUE_URL


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app_context = app.app_context()
    app_context.push()

    app.config.from_mapping(
        CELERY=dict(
            broker_url=QUEUE_URL,
            result_backend=QUEUE_URL,
            task_ignore_result=True,
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)
    db.init_app(app)
    db.create_all()
    return app
