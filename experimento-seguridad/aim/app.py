
from flask import Flask, request, jsonify
from configuracion import configuracion
import jwt
from typing import List, Dict, Optional

app = Flask(__name__)

# Clave secreta para firmar y verificar el token (debería ser segura y secreta en un entorno real)
SECRET_KEY = 'SPORTAPP_#20240301_MISO@JUPAAND'

# Base de datos simulada con información de usuarios y sus credenciales
credenciales_usuarios = [
    {"uuid": "15893de-bf0c-4978-9880-53a84fe08b94", "usuario": "usuario1", "password": "password1"},
    {"uuid": "488b2fc3-fb48-4549-8eaf-3c0ffca57c2a", "usuario": "usuario2", "password": "password2"}
]

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


