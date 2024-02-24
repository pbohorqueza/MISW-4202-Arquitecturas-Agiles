from flask import Flask, jsonify
from datetime import datetime

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

    if get_logs_counter % 10 == 0:
        response = {
            "message": "error",
            "status": "500",
            "status-timestamp": current_datetime
        }
    else:
        response =  {
            "message": "success",
            "status": "200",
            "status-timestamp": current_datetime,
            "data": {
                "deportista": "Pablo Garcia",
                "deporte": "ciclismo",
                "entrenamiento": {
                    "distancia-recorrida": "2m",
                    "ritmo-cardiaco": "ok"
                }
            }
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)