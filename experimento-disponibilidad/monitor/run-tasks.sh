#!/bin/bash

# ejecuta el sh
# chmod +x run-tasks.sh

# Corre el worker celery al que se subscribe el Monitor
celery -A tareas.tareas worker --loglevel=info -E 