# Mercado Inmuebles

Proyecto académico desarrollado durante el bootcamp de desarrollo
de aplicaciones con Python.

La aplicación permite consultar inmuebles disponibles para arriendo,
filtrarlos por región y comuna, registrar usuarios y administrar
propiedades desde un panel personal.

## Funcionalidades

- Registro, inicio y cierre de sesión.
- Actualización de datos del usuario.
- Consulta de inmuebles con filtros por región y comuna.
- Creación, actualización y eliminación de inmuebles propios.
- Confirmación antes de eliminar una propiedad.
- Administración mediante Django Admin.

## Tecnologías

- Python
- Django
- PostgreSQL
- HTML, CSS y Bootstrap

## Video de presentación

[Ver demostración de Mercado Inmuebles](https://www.youtube.com/watch?v=LVyT8yBE4VQ)

## Instalación y ejecución en Windows

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta que contiene manage.py.
3. Crear y activar un entorno virtual:

   python -m venv ambiente
   ambiente\Scripts\activate

4. Instalar las dependencias:

   python -m pip install -r requirements.txt

5. Crear una base de datos vacía en PostgreSQL.
6. Crear proyecto_inmuebles/settings_local.py con esta estructura,
   reemplazando los valores de ejemplo:

   SECRET_KEY = "clave-local-de-desarrollo"

   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": "nombre_de_la_base",
           "USER": "usuario_postgresql",
           "PASSWORD": "contraseña_postgresql",
           "HOST": "localhost",
           "PORT": "5432",
       }
   }

7. Aplicar las migraciones:

   python manage.py migrate

8. Cargar regiones, comunas y tipos de inmueble:

   python manage.py loaddata ubicaciones tipo_inmuebles

9. Crear un administrador:

   python manage.py createsuperuser

10. Iniciar el servidor:

    python manage.py runserver

11. Abrir http://127.0.0.1:8000/

Los usuarios e inmuebles se crean desde la aplicación o desde el
administrador. No se incluyen cuentas personales ni sus contraseñas.

## Autor

Diego Ignacio Rojas Díaz

[Perfil de GitHub](https://github.com/Prezin-Rojas)