from flask import Flask, jsonify
from datetime import datetime
from configuracion import configuracion
import requests

app = Flask(__name__)

# Variable global para contar llamadas a get_logs
get_logs_counter = 0


@app.route('/')
def index():
    return 'Component MonitoreoSaludDeportista is running'


@app.route('/getlogs')
def get_logs():
    global get_logs_counter
    get_logs_counter += 1

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    if get_logs_counter % configuracion['intervalo-peticiones-error'] == 0:
        response = {
            "message": "error",
            "status": "500",
            "status-timestamp": current_datetime
        }
    else:
        entrenamiento = requests.get(configuracion['entrenamiento-api-url'] + f"/{configuracion['entrenamiento-id']}")

        if entrenamiento.status_code == 200:
            response = {
                "message": "success",
                "status": "200",
                "status-timestamp": current_datetime,
                "data": entrenamiento.json()
            }
        else:
            response = {
                "message": "error en la petición a la API de entrenamientos",
                "status": "500",
                "status-timestamp": current_datetime
            }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=3001)
