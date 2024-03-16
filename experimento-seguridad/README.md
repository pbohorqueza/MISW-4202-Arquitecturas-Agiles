Experimento 2 (Seguridad) - Grupo 11 - Arquitecturas Agiles
==========================

## Instancia EC2 donde se pueden visualizar los logs:
http://ec2-35-170-224-6.compute-1.amazonaws.com:3000/logs


## Servicio AIM
Descripción componente: Este servicio expone 2 APIs: login y validar-token

El servicio de login recibe un request POST donde el body debe tener dos parametros en formato JSON (usuario y password)

ejemplo:

```
{
    "usuario": "usuario1",
    "password": "password1"
}
```

Si la combinación de usuario y password es válida se recibe el token JTW en la respuesta

ejemplo:
```
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMTU4OTNkZS1iZjBjLTQ5NzgtOTg4MC01M2E4NGZlMDhiOTQifQ.eGmAmQoGDr8Cf_WBKAtScUa5e7Y4gx9E24emidhb19U"
}
```

El servicio validar-token recibe un token JWT para ser validado. En caso de ser válido, devuelve las reglas de acceso asociadas al usuario existente en el contenido del token:

ejemplo:
```
{
    "reglas": "perfil-deportivo/deportista/salud",
    "uuid": "15893de-bf0c-4978-9880-53a84fe08b94"
}
```

## Servicio gestor-deportivo
Descripción componente: Este servicio expone un API llamado /consultar-perfil-deportivo el cual espera un token válido que debe ser generado a través del servicio AIM y su API /login

Si el token (JWT) es válido y está asociado a un usuario con las reglas de autorización válidas, se reponderá con la información asociada a la salud del deportista en su perfil deportivo. de lo contrario se responde con un error de autorización.

ejemplo de respuesta válida
```
{
    "perfil-deportivo": "xxx x xxxx xxx xxxx "
}
```

## Instalación del experimento:
1. Instale docker https://www.docker.com/products/docker-desktop/
2. Usando la terminal, ubíquese en la raiz de la carpeta experimento-seguridad
3. ejecute el siguiente comando:

```
docker-compose up
```

4. El servicio de AIM correrá en el puerto 3000 y el servicio gestor-deportivo en el puerto 3001
5. Para ejecutar los logs, se debe correr la aplicación xxxxx. Esta aplicación usa el archivo csv con un listado de usuarios con reglas validas e invalidas. Solo usuarios con la regla de acceso ‘perfil-deportivo/deportista/salud’ garantiza la visualización de los datos de salud del deportista
