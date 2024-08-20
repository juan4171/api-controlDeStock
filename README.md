# Django REST API for Control de stock Application

## Descripción

Este proyecto es una API REST creada con Django Rest Framework (DRF) en donde hago un CRUD de productos de una app de control de stock que luego sera "fronteneada" con react.

## Características

- La API permite crear, leer, actualizar y eliminar produtos y categorias de productos.
- Filtrado, búsqueda y ordenación de productos (proximamente).
- Autenticación de usuarios (proximamente).

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto localmente.

### Requisitos

- Python 3.x
- pip
- virtualenv (opcional pero recomendado)

### Pasos

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/api-controlDeStock.git
   cd api-controlDeStock
   ```
2. Crea y activa un entorno virtual:
  ```sh
   python venv venv
   env\Scripts\activate
  ```
3. Instala las dependencias:
  ```sh
   pip install -r requirements.txt
  ```
4. Realiza las migraciones de la base de datos:
  ```sh
   python manage.py migrate
  ```
5. Ejecuta el servidor de desarrollo:
  ```sh
   python manage.py runserver
  ```

Uso de Endpoints de producto (similar para las categorias)

Listar todas los productos
  ```sh
   GET /api/productos/
  ```
Crear nuevo producto
   ```sh
   POST /api/productos/
  ```
Obtener un producto específico
 ```sh
   GET /api/productos/{id}/
  ```
Actualizar un producto
  ```sh
   PUT /api/productos/{id}/
  ```
Eliminar un producto
  ```sh
   DELETE /api/productos/{id}/
  ```
