
from flask import Flask, jsonify
from celery import Celery
from tareas.tareas import subscribe_to_logs
import json
import os
import gevent
from gevent import monkey
import subprocess
import httpx
from redis import Redis
from configuracion import configuracion

monkey.patch_all()

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

LOGS_FILE = configuracion['logs-file']

@app.route('/')
def index():
    return 'Component Monitor is running'

# Envía la información de los logs al cliente (opcional)
@app.route('/logs')
def logs():
    if not os.path.exists(LOGS_FILE):
        # Si el archivo no existe, crearlo vacío
        with open(LOGS_FILE, 'a+') as file:
            json.dump([], file)
    elif os.path.getsize(LOGS_FILE) == 0:
        # Si el archivo está vacío, devolver un mensaje indicando que no hay datos
         with open(LOGS_FILE, 'a+') as file:
            json.dump([], file)
            return jsonify({'message': 'No logs available'})
    
    with open(LOGS_FILE, 'r') as f:
        response_data = json.load(f)

    return jsonify(response_data)


def run_monitor_ping_echo():
    redis = Redis(configuracion['redis-host'], configuracion['redis-port'], configuracion['redis-db'], configuracion['redis-password'])  # Conexión a Redis
    while True:
        print("Running monitor_ping_echo")
        
        # Realizar la solicitud HTTP para obtener los logs del componente MonitoreoSaludDeportista
        url = configuracion['monitoreo-salud-deportistas-host']
        response = httpx.get(url)
        
        # Publicar la respuesta en el canal de Redis
        redis.publish('log_channel', response.text)
        
        gevent.sleep(configuracion['segundos-ping'])  # Esperar x segundos antes de la próxima ejecución

gevent.spawn(subscribe_to_logs)
gevent.spawn(run_monitor_ping_echo)


if __name__ == '__main__':
    #por puerto 3000
    app.run(port=3000)
    
