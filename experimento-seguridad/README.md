Experimento 2 (Seguridad) - Grupo 11 - Arquitecturas Agiles
==========================

## Servicios corriendo en la instancia de EC2:

Link al servicio AIM en el servidor EC2 donde corre el API login (POST):

http://ec2-34-235-166-27.compute-1.amazonaws.com:3000/login


Link al servicio Gestor-Deportivo en el servidor EC2 donde corre el API consultar-perfil-deportivo (GET):

http://ec2-34-235-166-27.compute-1.amazonaws.com:3001/consultar-perfil-deportivo


## Servicio AIM
Descripción componente: Este servicio expone 2 APIs: login y validar-token

El servicio de login recibe un request POST donde el body debe tener dos parametros en formato JSON (usuario y password)

ejemplo de respuesta inválida de usuario no autorizado:

```
{
    "mensaje": "El usuario no cuenta con el nivel de acceso requerido"
}
```

ejemplo de respuesta válida:

```
[
    {
        "created_at": "2024-03-16T13:29:44",
        "historia_medica": "Poor method age international. Large beat pass include into purpose. Read scene thing wait.",
        "id": 1,
        "id_deportista": 717,
        "incapacidades": "Real dinner participant trip.",
        "lesiones": "General rate ahead expect skin behind daughter political."
    },
    {
        "created_at": "2024-03-16T13:29:44",
        "historia_medica": "Style activity food phone north court economy.",
        "id": 2,
        "id_deportista": 231,
        "incapacidades": "People between society buy paper.",
        "lesiones": "Serve long trade."
    },
    {
        "created_at": "2024-03-16T13:29:44",
        "historia_medica": "Police trade point TV enjoy. Say positive audience. Relationship throughout by mouth pull hair. Cup wind black information station manage use.",
        "id": 3,
        "id_deportista": 409,
        "incapacidades": "Fine wide cut argue activity house series.",
        "lesiones": "Alone value black speak."
    },
    {
        "created_at": "2024-03-16T13:29:44",
        "historia_medica": "Someone modern population past. Opportunity hot live nature then development field.",
        "id": 4,
        "id_deportista": 690,
        "incapacidades": "Meet issue follow point individual.",
        "lesiones": "Federal concern need person season."
    },
    {
        "created_at": "2024-03-16T13:29:44",
        "historia_medica": "Theory half body hot institution foreign. Size reason business again such. Change stop tough range.",
        "id": 5,
        "id_deportista": 618,
        "incapacidades": "Fish hard choose class.",
        "lesiones": "Perhaps down well industry."
    },
    {
        "created_at": "2024-03-16T13:29:44",
        "historia_medica": "Blood church various space market store center two. Hair every son ten.",
        "id": 6,
        "id_deportista": 507,
        "incapacidades": "Challenge others account ok those evidence.",
        "lesiones": "Mind lawyer accept house entire."
    },
    {
        "created_at": "2024-03-16T13:29:44",
        "historia_medica": "Growth discussion personal strategy agreement. However agent mission media stop finally.",
        "id": 7,
        "id_deportista": 606,
        "incapacidades": "Think white director dinner herself wide.",
        "lesiones": "Instead spring operation be visit marriage politics."
    },
    {
        "created_at": "2024-03-16T13:29:44",
        "historia_medica": "End central street network threat bring such enough. Ok officer paper growth.",
        "id": 8,
        "id_deportista": 265,
        "incapacidades": "There mission follow add eye spend those.",
        "lesiones": "Piece investment hot effect."
    },
    {
        "created_at": "2024-03-16T13:29:44",
        "historia_medica": "Statement right describe answer teach positive do care. Treatment benefit floor no.",
        "id": 9,
        "id_deportista": 719,
        "incapacidades": "Building PM world major.",
        "lesiones": "Though particular authority red national country away."
    },
    {
        "created_at": "2024-03-16T13:29:44",
        "historia_medica": "Group night civil eight idea and. List seek girl political street. Black writer hard husband although up while.",
        "id": 10,
        "id_deportista": 625,
        "incapacidades": "Themselves professor a middle care TV across.",
        "lesiones": "Clearly hair woman."
    }
]
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

## Instalación del experimento y ejecución de logs:
1. Instale docker https://www.docker.com/products/docker-desktop/
2. Usando la terminal, ubíquese en la raiz de la carpeta experimento-seguridad
3. ejecute el siguiente comando:

```
docker-compose up
```

4. El servicio de AIM correrá en el puerto 3000 y el servicio gestor-deportivo en el puerto 3001
5. Para ejecutar los logs, se debe correr la aplicación ubicad en la carpeta logger. Esta aplicación usa el archivo users.csv con un listado de usuarios con reglas validas e invalidas. Solo usuarios con la regla de acceso ‘perfil-deportivo/deportista/salud’ garantiza la visualización de los datos de salud del deportista y una respuesta válida 200. Usuarios sin reglas de acceso válidas retornan un error 401.

Ubíquese en la carpeta logger y cree un ambiente virtual de pyhton en la carpeta

    python -m venv venv

Active el entorno virtual

    source venv/bin/activate

Instale las dependencias

    pip install -r requirements.txt

Ejecute los logs:

    python3 main.py


Los logs se generarán en el archivo request_log.txt
