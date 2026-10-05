# Tasks FastAPI

Proyecto de ejemplo implementado con FastAPI, utilizando PostgreSQL como base de datos.

## Arquitectura

El proyecto sigue una arquitectura por capas:

- **models**: Definición de modelos de base de datos (SQLAlchemy)
- **schemas**: Definición de esquemas Pydantic para validación de datos
- **repositories**: Lógica de acceso a datos
- **services**: Lógica de negocio
- **routers**: Definición de endpoints y rutas de la API
- **db**: Configuración de conexión a base de datos

## Requisitos Previos

- Python 3.8+
- PostgreSQL
- Docker (opcional, para contenedores)

## Instalación

1. Crear entorno virtual:
```bash
python -m venv .venv
```

2. Activar entorno virtual:
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install fastapi uvicorn sqlalchemy psycopg[binary]
```

## Configuración de Base de Datos

### Opción 1: Usar Docker Compose

```bash
docker-compose up -d
```

Esto iniciará:
- PostgreSQL en puerto 5432
- pgAdmin en puerto 5050 (http://localhost:5050)

Credenciales pgAdmin:
- Email: admin@admin.com
- Password: admin

### Opción 2: PostgreSQL Local

Asegúrate de tener PostgreSQL instalado y configurado con las credenciales especificadas en `db.py`:
- Usuario: postgres
- Password: postgres
- Base de datos: postgres
- Puerto: 5432

## Ejecutar el Proyecto

### Desarrollo (con recarga automática):

```bash
uvicorn main:app --reload
```

### Producción:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

La API estará disponible en: http://localhost:8000

## Documentación de la API

FastAPI genera automáticamente la documentación interactiva:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Comandos Útiles de Python

### Gestión de Entorno Virtual

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual (Windows)
.venv\Scripts\activate

# Activar entorno virtual (Linux/Mac)
source .venv/bin/activate

# Desactivar entorno virtual
deactivate

# Ver paquetes instalados
pip list

# Guardar dependencias
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt
```

### Ejecución

```bash
# Ejecutar aplicación con recarga automática
uvicorn main:app --reload

# Ejecutar en puerto específico
uvicorn main:app --port 8080

# Ejecutar con debug
uvicorn main:app --reload --log-level debug
```

### Base de Datos

```bash
# Iniciar contenedores Docker
docker-compose up -d

# Ver logs de contenedores
docker-compose logs -f

# Detener contenedores
docker-compose down

# Detener y eliminar volúmenes
docker-compose down -v
```

## Estructura del Proyecto

```
ejemplo-fastapi2/
├── main.py              # Punto de entrada de la aplicación
├── db.py                # Configuración de base de datos
├── docker-compose.yaml  # Configuración Docker
├── models/              # Modelos SQLAlchemy
├── schemas/             # Esquemas Pydantic
├── repositories/        # Repositorios de datos
├── services/            # Lógica de negocio
└── routers/             # Rutas de la API
```
