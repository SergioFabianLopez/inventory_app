# API REST de Inventario de Alimentos y Bebidas (Django)

Este proyecto implementa una API REST para un sistema de inventarios de Alimentos y Bebidas, utilizando Django y Django REST Framework, con SQLite como base de datos en memoria.

## Requisitos

* Python 3.8+

## Configuración e Instalación

1.  **Clonar el repositorio y navegar al directorio del proyecto:**
    ```bash
    cd inventory_app
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    # En Windows:
    python -m venv venv
    # venv\Scripts\activate
    # En macOS/Linux:
    python3 -m venv venv
    # source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar migraciones:**
    ```bash
    python manage.py makemigrations inventory_api
    python manage.py migrate
    ```

## Ejecutar la Aplicación

Para iniciar el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

## Endpoints principales

| Método | Endpoint               | Descripción                    |
|--------|------------------------|--------------------------------|
| GET    | /api/food-drinks/      | Lista de comidas y bebidas     |
| POST   | /api/food-drinks/      | Crear nuevo producto           |
| GET    | /api/food-drinks/<id>/ | Obtener producto específico    |
| PUT    | /api/food-drinks/<id>/ | Actualizar producto            |
| DELETE | /api/food-drinks/<id>/ | Eliminar producto              |


### Crear un nuevo producto

```bash
curl -X POST http://127.0.0.1:8000/api/food-drinks/ \
    -H "Content-Type: application/json" \
    -d '{"name": "Pizza Margherita", "status": true}'
```

### Actualizar producto

```bash
curl -X PUT http://127.0.0.1:8000/api/food-drinks/1/ \
    -H "Content-Type: application/json" \
    -d '{"status": false}'
```

## Documentación interactiva

Accede a Swagger UI en:
```
http://127.0.0.1:8000/api/docs/
```

## Correr Test
```
python manage.py test inventory_api
```