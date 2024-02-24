#!/bin/bash

# Corre el worker celery al que se subscribe el Monitor
celery -A tareas.tareas worker --loglevel=info -E 