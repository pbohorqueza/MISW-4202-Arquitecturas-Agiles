import redis
from celery import Celery
import json
import os
from datetime import datetime
from configuracion import configuracion

LOGS_FILE = configuracion['logs-file']

celery = Celery('tasks', broker=f"redis://{configuracion['redis-host']}:{configuracion['redis-port']}/{configuracion['redis-db']}")

@celery.task(name='process_log')
def process_log(log_data):
    
    # Procesar el log recibido, por ejemplo, simplemente devolverlo como está
    # o procesarlo para que tenga un formato específico
    # ejemplos de respuestas:

    # Ejemplo de respuesta correcta esperada:
    #
    # {
    #     "message": "success",
    #     "status": "200",
    #     "status-timestamp": "23349447474",
    #     "data": {
    #         "deportista": "Juan",
    #         "deporte": "ciclismo",
    #         "entrenamiento": {
    #             "distancia-recorrida": "2m",
    #             "ritmo-cardiaco": "ok"
    #         }
    #     }
    # }

    # Ejemplo de respuesta incorrecta esperada:
    # {
    #    "message": "error",
    #    "status": "500",
    #    "status-timestamp": "23349447474"
    # }

    # return log_data
    print("called process_log!!!")
    
    # Set the status timestamp to the current time
    log_data['log-timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Diferencia de tiempo entre el momento en que se recibe el log y el momento en que se generó el log
    difference_dates = datetime.strptime(log_data['log-timestamp'], "%Y-%m-%d %H:%M:%S.%f") - datetime.strptime(log_data['status-timestamp'], "%Y-%m-%d %H:%M:%S.%f")
    difference_in_milliseconds = difference_dates.total_seconds() * 1000
    
    log_data['miliseconds-latency'] = str(difference_in_milliseconds)
            
    # Cargar el contenido actual del archivo si existe
    if os.path.exists(LOGS_FILE):
        with open(LOGS_FILE, 'r') as f:
            logs = json.load(f)
    else:
        logs = []

    # Agregar la nueva entrada al arreglo de logs
    logs.append(log_data)

    # Escribir el contenido actualizado al archivo
    with open(LOGS_FILE, 'w') as f:
        json.dump(logs, f)


def subscribe_to_logs():
    print("Subscribiéndose al broker de mensajes...")
    redis_client = redis.StrictRedis(host=configuracion['redis-host'], port=configuracion['redis-port'], db=configuracion['redis-db'])
    pubsub = redis_client.pubsub()
    pubsub.subscribe('log_channel')
    for item in pubsub.listen():
        print("Mensaje recibido:", item)
        if item['type'] == 'message':
            log_data = json.loads(item['data'])
            process_log.delay(log_data)