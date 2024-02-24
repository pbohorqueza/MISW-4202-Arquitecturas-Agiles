from config import FLASK_PORT, FLASK_DEBUG
from factories.flask_factory import create_app
from models.entrenamiento import Entrenamiento
from models.schemas.entrenamiento_schema import EntrenamientoSchema

app = create_app()


@app.route("/")
def index():
    entrenamientos = Entrenamiento.query.all()
    schema = EntrenamientoSchema()

    return schema.dump(entrenamientos, many=True)


@app.route("/<int:id_entrenamiento>")
def show(id_entrenamiento):
    entrenamiento = Entrenamiento.query.get(id_entrenamiento)
    schema = EntrenamientoSchema()
    schema.context = {
        "load_deportista": True,
        "load_deporte": True,
    }

    return schema.dump(entrenamiento)


@app.route("/deportistas/<int:id_deportista>/entrenamientos")
def deportista_entrenamientos(id_deportista):
    schema = EntrenamientoSchema()
    entrenamientos = Entrenamiento.query.filter_by(id_deportista=id_deportista).all()

    return schema.dump(entrenamientos, many=True)


if __name__ == "__main__":
    app.run(debug=FLASK_DEBUG, port=FLASK_PORT)
