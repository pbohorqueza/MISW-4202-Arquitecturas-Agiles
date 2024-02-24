# Deportes Micro-servicio

Es una simple api para el manejo de deportes.

## Endpoints

- GET /deportes
- GET /deportes/{id}

## Configuración

### Ambiente de desarrollo

#### Docker

#### Local

Para correr el proyecto localmente, solo es necesario crear un `virtualenv` e instalar las dependencias.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Variables de entorno

Primero, se deben configurar las variables de entorno. Para ello, se debe crear un archivo `.env` en la raíz del
proyecto. El proyecto ya provee un archivo `.env.example` que se puede copiar y modificar.

```bash
cp .env.example .env
```

Luego, se deben modificar las variables de entorno según sea necesario.

### Popular la base de datos

Para popular la base de datos, se debe correr el siguiente comando:

```bash
python seeder.py
```

Cabe mencionar que es necesario haber configurado las variables de entorno y haber instalado las dependencias.

## Correr el proyecto

Una vez configuradas las variables de entorno y populada la base de datos, se puede correr el proyecto con el siguiente
comando:

```bash
python app.py
```

De manera predeterminada, el proyecto correrá en el puerto `5003`. Para cambiar el puerto, se debe modificar la variable
de entorno `FLASK_PORT` en el archivo `.env`.
