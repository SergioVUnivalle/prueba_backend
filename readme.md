# 🧪 Prueba Técnica Backend - Django + PostgreSQL

## 📝 Instrucciones Generales

Este proyecto tiene como objetivo evaluar el uso de buenas prácticas en el desarrollo con Django, el manejo de datos geoespaciales y la implementación de APIs seguras y funcionales.

Se valorará:

- Una estructura de proyecto clara y modular.
- El uso correcto del ORM de Django.
- La integración adecuada de herramientas del ecosistema Django.
- La documentación clara de lo realizado en este archivo README.md para ejecutar el proyecto localmente.

> La entrega debe enviarse al correo desde el cual fue enviada la prueba, incluyendo:
> - Backup de la base de datos.
> - Ruta del repositorio del código fuente.
> - Cualquier otro archivo requerido para el despliegue local.

## ⚙️ Requisitos de Implementación

### 🔧 Configuración del entorno

2. Configurar un entorno virtual local e instalar los paquetes necesarios incluidos en el proyecto.

3. Configurar la conexión a una base de datos PostgreSQL local con la extensión PostGIS habilitada. Utilizar el conector psycopg y ejecutar las migraciones del proyecto.

### 🏗️ Estructura del proyecto

4. Modificar la estructura base del proyecto en Django para garantizar una organización clara y modular de las carpetas. Se recomienda el uso de variables de entorno o la implementacion de archivos secrets o variable de entorno para gestionar configuraciones sensibles, siguiendo las buenas prácticas de despliegue de Django.

5. Dentro del proyecto, se deben crear dos aplicaciones:
   - Una aplicación para almacenar los modelos de datos.
   - Una aplicación dedicada a la API.

### 🗂️ Datos geográficos

6. Cargar el archivo .shp de municipios y el archivo .shp de oficinas, generando los modelos correspondientes en Django con soporte geoespacial.

### 🔐 Autenticación

7. Usar el estándar JWT para implementar un endpoint de autenticación que reciba el nombre de usuario y la contraseña, y retorne el token de acceso y refresco.

### 🧩 APIs requeridas

8. Implementar un endpoint (usando Django Rest Framework) que reciba el nombre de un departamento y retorne la lista de municipios que lo componen. Este endpoint debe estar protegido contra accesos no autenticados.

10. Implementar un endpoint geográfico que reciba el ID de una oficina y retorne la geometría del municipio donde se encuentra, en formato GeoJSON.

---

💡 Se recomienda mantener el código limpio, comentado y seguir los principios de desarrollo sostenible.






# Prueba Técnica - Backend GIS con Django y PostGIS

Este proyecto es una API REST construida con Django 5.2.1, diseñada para manejar datos geográficos usando PostGIS y QGIS. Incluye autenticación con JWT y funcionalidades geoespaciales expuestas a través de endpoints protegidos.

---

## Tecnologías utilizadas

Python 3.12
Django 5.2.1
Django REST Framework
PostGIS (PostgreSQL)
QGIS 3.34 - GDAL
JWT Authentication

---

## Pasos para ejecutar el proyecto

### Requisitos

Python 3.12 o superior
PostgreSQL con extensión **PostGIS**  
virtualenv  
Git  

---

### Configuración inicial

1. **Clonar el repositorio:**

git clone
cd PRUEBAINGRESO_BACK

# Crear el ambiente
python -m venv venv
# Activar ambiente
source venv/bin/activate  # En Windows: venv\Scripts\activate
# Instalar requerimientos
pip install -r requirements.txt

CREATE DATABASE prueba_tecnica;
\c prueba_tecnica
CREATE EXTENSION postgis;


## Endpoints desarrollados
Autenticación con JWT

# GET /api/municipios/<nombre_departamento>/
Retorna los municipios del departamento dado.

# GET /api/oficina/<id>/municipio/
Retorna la geometría en formato GeoJSON del municipio en el que se encuentra la oficina con el ID indicado.

Notas adicionales
La versión de Django requerió una versión de GDAL, se usó el  Python de QGIS 3.34.13 para el uso de GDAL
