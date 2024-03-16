from factories import create_app
from flask import Flask, request, jsonify
import jwt
import requests
from config import AIM_URL
from models.perfildeportivo import PerfilDeportivo
from models.schemas.perfildeportivo_schema import PerfilDeportivoSchema
from config import FLASK_PORT, FLASK_DEBUG

app = create_app()

@app.route('/')
def index():
    return "Gestor Deportivo service"

@app.route("/consultar-perfil-deportivo")
def get_perfiles():
    authorization_token = request.headers.get('Authorization')
    url = AIM_URL + "/validar-token"
    headers = {
        "Authorization": f"{authorization_token}"
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        
        valores = response.json()
        reglas = valores.get('reglas')

        if reglas == 'perfil-deportivo/deportista/salud':
            perfiles = PerfilDeportivo.query.all()
            schema = PerfilDeportivoSchema()
            return schema.dump(perfiles, many=True),200
        else:
            return jsonify({"mensaje": "El usuario no cuenta con el nivel de acceso requerido"}), 401

    else:
       return jsonify(response.text), 500
   
    
    




