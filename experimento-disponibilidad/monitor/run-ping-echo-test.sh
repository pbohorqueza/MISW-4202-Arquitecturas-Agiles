#!/bin/bash

# Este archivo es solo para hacer ping desde la consola. No es necesario para el funcionamiento del sistema.

chmod +x run-ping-echo.sh

# Ping echo para preguntar por los logs del componente MonitoreoSaludDeportista
response=$(curl -s http://localhost:3001/getlogs)

# Publica la respuesta al canal de Redis usando redis-cli
redis-cli PUBLISH log_channel "$response"