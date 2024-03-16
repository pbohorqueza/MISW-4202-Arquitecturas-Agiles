import os

from flask import Flask

from models.database import db
from config import DATABASE_URL


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app_context = app.app_context()
    app_context.push()


    db.init_app(app)
    db.create_all()
    return app
