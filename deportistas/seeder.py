from models.deportista import Deportista
from app import app

if __name__ == "__main__":
    with app.app_context():
        Deportista.factory().create(10)

