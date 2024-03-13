from config import FLASK_PORT, FLASK_DEBUG
from factories.flask_factory import create_app
from models.deporte import Deporte
from models.schemas.deporte_schema import DeporteSchema

app = create_app()


@app.route("/")
def index():
    deportes = Deporte.query.all()
    schema = DeporteSchema()

    return schema.dump(deportes, many=True)


@app.route("/<int:id_deporte>")
def show(id_deporte):
    deporte = Deporte.query.filter_by(id=id_deporte).one_or_none()
    schema = DeporteSchema()

    if not deporte:
        return {"mensaje": "Deporte no encontrado"}, 404

    return schema.dump(deporte)


if __name__ == "__main__":
    app.run(debug=FLASK_DEBUG, port=FLASK_PORT)
