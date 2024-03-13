from factories import create_app
from models.deportista import Deportista
from models.schemas import DeportistaSchema
from config import FLASK_PORT, FLASK_DEBUG

app = create_app()


@app.route("/")
def index():
    deportistas = Deportista.query.all()
    schema = DeportistaSchema()

    return schema.dump(deportistas, many=True)


@app.route("/<int:id_deportista>")
def show(id_deportista):
    schema = DeportistaSchema()
    deportista = Deportista.query.filter_by(id=id_deportista).one_or_none()

    if not deportista:
        return {"mensaje": "Deportista no encontrado"}, 404

    return schema.dump(deportista)


@app.route("/<int:id_deportista>/entrenamientos")
def show_entrenamientos(id_deportista):
    deportista = Deportista.query.filter_by(id=id_deportista).one_or_none()
    schema = DeportistaSchema()

    if not deportista:
        return {"mensaje": "Deportista no encontrado"}, 404

    schema.context = {
        "load_entrenamientos": True,
    }

    return schema.dump(deportista)


if __name__ == "__main__":
    app.run(debug=FLASK_DEBUG, port=FLASK_PORT)
