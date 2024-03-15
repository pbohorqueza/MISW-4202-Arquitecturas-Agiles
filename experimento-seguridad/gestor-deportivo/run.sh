#!/bin/bash

# Seed de la base de datos
python seeder.py

# Correr la app
flask run -h 0.0.0.0