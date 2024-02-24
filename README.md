Experimento 1 grupo 11 - Arquitecturas Agiles
==========================

## Componente MonitoreoSaludDeportista
Este componente se encarga de devolver el estado de salud del deportista. Para propósitos del experimento, genera una respuesta con datos correctos, y cada cierto número de peticiones genera una respuesta de error.
Para modificar este intervalo, modifique el valor en el archivo configuracion.py

Ejemplos de respuesta:
```
{
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
```

```
{
    "message": "error",
    "status": "500",
    "status-timestamp": current_datetime
}
```


### Instalación del microservicio:

Ubíquese en la carpeta monitoreo-salud-deportista y cree un ambiente virtual de pyhton en la carpeta

    python -m venv venv

Active el entorno virtual

    source venv/bin/activate


Para ejecutar el componente, agregue permisos de escritura al archivo run.sh

    chmod +x run.sh

Y luego ejecútelo

    ./run.sh

El componente estará ejecutado en el puerto 3001. la información es expuesta en la siguiente ruta:
http://127.0.0.1:3001/getlogs


## Componente Monitor > tarea asíncrona de conexión al broker de Redis
Esta tarea se conecta al servidor de redis, tiene la funcionalidad tanto para la subscripción como para la publicación y el procesamiento de la respuesta

### Instalación de la tarea:

Asegúrese de tener el entorno virtual configurado para este microservicio. Ubíquese en la carpeta monitor y ejecute:

    python -m venv venv

Active el entorno virtual

    source venv/bin/activate



Luego corra el archivo run-tasks.sh asegúrandose de que el archivo tiene permisos de ejecución

    chmod +x run-tasks.sh
    
    run-tasks.sh


## Componente Monitor
Este componente se encarga de invocar la subscripción de la tarea, y de hacer ping-echo al componente monitoreo-salud-deportistas-host cada intervalo de tiempo para conocer el estado de salud del componente.
Igualmente se encarga de consolidar el reporte. para configurar el intervalo del ping-echo, modifique el valor *segundos-ping* en el archivo configuracion.py. 
En el archivo de configuración.py puede modificar los accesos al servidor de Redis, así como la ubicación del archivo donde se escriben los logs:

```
configuracion = {
    "monitoreo-salud-deportistas-host": "http://localhost:3001/getlogs",
    "segundos-ping": 5,
    "redis-host": "localhost",
    "redis-port": 6379,
    "redis-db": 0,
    "logs-file": "logs.json"
}
```

De igual manera este componente expone un API para visualización de los logs.

### Instalación del microservicio:

Ubíquese en la carpeta monitor. Para ejecutar el componente, agregue permisos de escritura al archivo run-monitor.sh

    chmod +x run-monitor.sh

Y luego ejecútelo

    ./run-monitor.sh

Este componente estará ejecutado en el puerto 3000. Si quiere revisar los logs, puede ir a la ruta
http://127.0.0.1:3000/logs


Nota: Los logs generados incluyen la diferencia en milisegundos entre el momento en que se genera la respuesta, ya sea válida o de error del componente MonitoreoSaludDeportista, y el momento en que se genera el log que visualizará el administrador. Esto permite validar la medida de respuesta que se espera para el propósito de experimento, la cual debe ser no mayor a 2000 milisegundos (2 segundos)

Ejemplo:

```
[{
    "message": "error",
    "status": "500",
    "status-timestamp": "2024-02-24 09:52:27.406349",
    "log-timestamp": "2024-02-24 09:52:27.415203",
    "miliseconds-latency": "8.854000000000001"
  },
  {
    "data": {
      "deporte": "ciclismo",
      "deportista": "Pablo Garcia",
      "entrenamiento": { "distancia-recorrida": "2m", "ritmo-cardiaco": "ok" }
    },
    "message": "success",
    "status": "200",
    "status-timestamp": "2024-02-24 09:52:32.441207",
    "log-timestamp": "2024-02-24 09:52:32.450407",
    "miliseconds-latency": "9.2"
  }]
```
