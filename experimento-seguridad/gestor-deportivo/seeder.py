from models.perfildeportivo import PerfilDeportivo
from app import app

if __name__ == "__main__":
    with app.app_context():
        PerfilDeportivo.factory().create(1)

