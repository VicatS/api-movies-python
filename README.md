# Movie Catalog API

Esta es una API de catálogo de películas desarrollada con Flask y SQLAlchemy. Permite crear, leer, actualizar y eliminar (CRUD) películas, así como subir imágenes para las portadas de las películas.

## Requisitos

- Python 3.10+
- MySQL
- Instalar pip para la descarga de dependencias y librerias

## Configuración del Entorno

1. Clona este repositorio:

   ```bash
   git clone https://github.com/VicatS/api-movies-python.git
   cd api-movies-python

2. Crea un entorno virtual e instálalo:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

3.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt

4. Configura las variables de entorno. Crea un archivo .env en la raíz del proyecto y añade tus configuraciones:

    ```bash
    FLASK_APP=run.py
    FLASK_ENV=development
    DATABASE_URL=mysql+pymysql://username:password@localhost/dbname
    UPLOAD_FOLDER=./app/static/uploads

## Base de datos

1. Configura tu base de datos MySQL y actualiza la URL de la base de datos en el archivo .env.
2. Crea la base de datos

    ```sql
    CREATE DATABASE dbname;
3. Inicializa la base de datos:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade

## Ejecutar la Aplicación

1. Activa el entorno virtual si no lo has hecho:

    ```bash
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

2. Ejecuta la aplicación:

    ```bash
    flask run

## Endpoints de la API

1.  Obtener Todas las Películas

    ```http
    GET /api/v1/movies

2.  Obtener una Película por ID

    ```http
    GET /api/v1/movies/{id}

3.  Crear una Nueva Película

    ```http
    POST /api/v1/movies

Parámetros del Formulario
- `name` (string): Nombre de la película (requerido)
- `cover_image` (file): Imagen de la portada de la película (requerido)
- `classification` (string): Clasificación de la película (requerido)
- `genre` (string): Género de la película (requerido)
- `release_date` (date): Fecha de estreno de la película (requerido)
- `synopsis` (string): Sinopsis de la película (requerido)

4.  Actualizar una Película

    ```http
    PUT /api/v1/movies/{id}

Parámetros del Formulario
- `name` (string): Nombre de la película
- `cover_image` (file): Imagen de la portada de la película
- `classification` (string): Clasificación de la película
- `genre` (string): Género de la película
- `release_date` (date): Fecha de estreno de la película
- `synopsis` (string): Sinopsis de la película

5.  Eliminar una Película    

    ```http
    DELETE /api/v1/movies/{id}

## Subir y Mostrar Imágenes

- Las imágenes se suben al directorio configurado en UPLOAD_FOLDER. Para acceder a una imagen, usa la siguiente URL:

    ```http
    GET /static/uploads/{filename}

## Importacion archivo .json para pruebas de la API en Postman

1.  Descargar el archivo .json `movie_catalog_api_collection.json` desde la carpeta `postman` desde el proyecto.
2.  Seleccionar la opcion `Import` en Postman.
3.  Escoger el archivo `movie_catalog_api_collection.json`.
4.  Dar `Importar`

## Estructura del Proyecto

```plaintext
.
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── movie_controller.py
│   ├── extensions/
│   │   ├── __init__.py
│   │   └── extensions.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── movie.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── movie_route.py
│   ├── serializers/
│   │   ├── __init__.py
│   │   └── movie_serializer.py
│   ├── static/
│   │   └── uploads/
│   └── templates/
│       └── index.html
├── migrations/
│   ├── ...
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
