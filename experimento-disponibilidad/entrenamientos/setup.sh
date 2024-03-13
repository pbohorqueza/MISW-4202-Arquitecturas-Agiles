#!/bin/bash

# crear entorno virtual si no existe
if [ ! -d ".venv" ]; then
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
fi

# Seed de la base de datos
python seeder.py

# Correr el servidor
python app.py