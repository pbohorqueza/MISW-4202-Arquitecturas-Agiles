from factories import create_app
from models.perfildeportivo import PerfilDeportivo
from models.schemas.perfildeportivo_schema import PerfilDeportivoSchema
from config import FLASK_PORT, FLASK_DEBUG

app = create_app()

@app.route('/')
def index():
    return "Gestor Deportivo service"

@app.route("/perfiles")
def get_perfiles():
    perfiles = PerfilDeportivo.query.all()
    schema = PerfilDeportivoSchema()

    return schema.dump(perfiles, many=True)




