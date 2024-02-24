from models.entrenamiento import Entrenamiento
from app import app

if __name__ == "__main__":
    with app.app_context():
        Entrenamiento.factory().create(10)

