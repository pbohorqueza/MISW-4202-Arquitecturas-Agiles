from models.deporte import Deporte
from app import app

if __name__ == "__main__":
    with app.app_context():
        Deporte.factory().create(10)

