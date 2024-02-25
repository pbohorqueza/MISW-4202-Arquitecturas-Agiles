from factories import celery_factory, flask_factory

flask_app = flask_factory.create_app()
celery_app = celery_factory.celery_init_app(flask_app)
