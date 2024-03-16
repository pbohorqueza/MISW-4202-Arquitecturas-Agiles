
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

# Base de datos simulada con información de usuarios y sus credenciales
credenciales_usuarios = [
    {"uuid": "15893de-bf0c-4978-9880-53a84fe08b94", "usuario": "usuario1", "password": "password1", "reglas": "perfil-deportivo/deportista/salud"},
    {"uuid": "488b2fc3-fb48-4549-8eaf-3c0ffca57c2a", "usuario": "usuario2", "password": "password2", "reglas": "perfil-demografico/deportista/pais"},
    {"uuid": "ce5b2145-5e00-464f-81b7-484152955bcd", "usuario": "usuario3", "password": "password3", "reglas": "entrenamiento/deportista/estado-fisico"},
    {"uuid": "e5aa3d12-15e3-4d04-830c-25277c959e4b", "usuario": "usuario4", "password": "password4", "reglas": "facturacion/socio/logistica"},
    {"uuid": "9f64e7c3-e89d-4b49-bb43-0d3a1107b83a", "usuario": "usuario5", "password": "password5", "reglas": "perfil-deportivo/deportista/salud"}
]

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
    autorizar_usuario = verificar_credenciales(usuario, password, credenciales_usuarios)
    if autorizar_usuario is not None:
        # Generar el token JWT con información sobre los permisos del usuario
        token_payload = {
            "uuid": autorizar_usuario.get("uuid")
        }
        token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')

        return jsonify({"token": token})
    else:
        return jsonify({"mensaje": "Credenciales inválidas"}), 401
    
def verificar_credenciales(usuario: str, password: str, usuarios: List[Dict[str, str]]) -> Optional[Dict[str, str]]:
    usuario = next(filter(lambda x: x.get("usuario") == usuario and x.get("password") == password, usuarios), None)
    return usuario




class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    reglas = db.Column(db.String(50), unique=False, nullable=False)

    def _repr_(self):
        return '<Usuario %r>' % self.usuario

# Ruta para consultar un usuario por nombre y contraseña
@app.route('/consulta_usuario', methods=['POST'])
def consulta_usuario():
    data = request.json
    usuario = data.get('usuario')
    password = data.get('password')
    
    usuario_encontrado = Usuario.query.filter_by(usuario=usuario, password=password).first()
    
    if usuario_encontrado:
        return jsonify({'mensaje': 'Usuario encontrado'})
    else:
        return jsonify({'mensaje': 'Usuario no encontrado'})



with app.app_context():
    db.create_all()
