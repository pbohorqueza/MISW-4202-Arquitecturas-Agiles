
from flask import Flask, request, jsonify
import jwt
from typing import List, Dict, Optional
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'usuarios.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db = SQLAlchemy(app)


# Clave secreta para firmar y verificar el token (debería ser segura y secreta en un entorno real)
SECRET_KEY = 'SPORTAPP_#20240301_MISO@JUPAAND'

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    reglas = db.Column(db.String(50), unique=False, nullable=False)

    def _repr_(self):
        return '<Usuario %r>' % self.usuario

@app.route('/')
def index():
    return "AIM service"

@app.route('/validar-token', methods=['POST'])
def validar_token():
    auth_header = request.headers.get('Authorization')

    # Verificar si se proporcionó un encabezado de autorización
    if not auth_header:
        return jsonify({"mensaje": "Token no proporcionado"}), 401

    # Verificar si el encabezado de autorización está en el formato correcto
    partes = auth_header.split()
    if len(partes) != 2 or partes[0].lower() != 'bearer':
        return jsonify({"mensaje": "Encabezado de autorización inválido"}), 401

    # Obtener el token de las partes
    token = partes[1]

    # Decodificar y verificar el token
    try:
        token_payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        usuario_id = token_payload.get('uuid')
        usuario = Usuario.query.filter_by(uuid=usuario_id).first()
        
        if usuario:
            return jsonify({"uuid": usuario_id, "reglas": usuario.reglas}), 200
        else:
            return jsonify({"mensaje": "Usuario inválido"}), 401 
    except jwt.ExpiredSignatureError:
        return jsonify({"mensaje": "Token expirado"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"mensaje": "Token inválido"}), 401

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    password = datos.get('password')

    # Verificar las credenciales del usuario
    autorizar_usuario = verificar_credenciales(usuario, password)
    if autorizar_usuario is not None:
        # Generar el token JWT con información sobre los permisos del usuario
        token_payload = {
            "uuid": autorizar_usuario.uuid
        }
        token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')

        return jsonify({"token": token})
    else:
        return jsonify({"mensaje": "Credenciales inválidas"}), 401
    
def verificar_credenciales(usuario: str, password: str) -> Usuario:
    usuario = Usuario.query.filter_by(usuario=usuario, password=password).first()
    return usuario

with app.app_context():
    db.create_all()
