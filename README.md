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
pip install fastapi uvicorn sqlalchemy psycopg[binary] pydantic-settings
```

4. Configurar variables de entorno:
```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar .env con tus credenciales de base de datos
```

Las variables de entorno disponibles son:
- `DB_DRIVER`: Driver de base de datos (default: postgresql+psycopg)
- `DB_USERNAME`: Usuario de base de datos (default: postgres)
- `DB_PASSWORD`: Contraseña de base de datos (default: postgres)
- `DB_HOST`: Host de base de datos (default: localhost)
- `DB_PORT`: Puerto de base de datos (default: 5432)
- `DB_NAME`: Nombre de la base de datos (default: postgres)

## Configuración de Base de Datos

### Opción 1: Usar Docker Compose

1. Configurar variables de entorno para Docker:
```bash
# Copiar el archivo de ejemplo
cp .env.docker.example .env.docker

# Editar .env.docker con tus credenciales deseadas
```

Las variables de entorno disponibles para Docker son:
- `POSTGRES_USER`: Usuario de PostgreSQL (default: postgres)
- `POSTGRES_PASSWORD`: Contraseña de PostgreSQL (default: postgres)
- `POSTGRES_DB`: Nombre de la base de datos (default: postgres)
- `POSTGRES_PORT`: Puerto de PostgreSQL (default: 5432)
- `PGADMIN_DEFAULT_EMAIL`: Email para pgAdmin (default: admin@admin.com)
- `PGADMIN_DEFAULT_PASSWORD`: Contraseña para pgAdmin (default: admin)
- `PGADMIN_PORT`: Puerto de pgAdmin (default: 5050)

2. Iniciar los contenedores:
```bash
docker compose --env-file .env.docker up -d
```

Esto iniciará:
- PostgreSQL en el puerto configurado (default: 5432)
- pgAdmin en el puerto configurado (default: 5050, accesible en http://localhost:5050)

Credenciales pgAdmin (se configuran en .env):
- Email: admin@admin.com
- Password: admin

### Opción 2: PostgreSQL Local

Asegúrate de tener PostgreSQL instalado y configura las credenciales en el archivo `.env`:
- Usuario: postgres
- Password: postgres
- Base de datos: postgres
- Puerto: 5432

## Ejecutar el Proyecto

### Desarrollo (con recarga automática):

```bash
python -m uvicorn main:app --reload
```

### Producción:

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
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
python -m uvicorn main:app --reload

# Ejecutar en puerto específico
python -m uvicorn main:app --port 8080

# Ejecutar con debug
python -m uvicorn main:app --reload --log-level debug
```

### Base de Datos

```bash
# Iniciar contenedores Docker
docker compose --env-file .env.docker up -d

# Ver logs de contenedores
docker compose --env-file .env.docker logs -f

# Detener contenedores
docker compose --env-file .env.docker down

# Detener y eliminar volúmenes
docker compose --env-file .env.docker down -v
```

## Estructura del Proyecto

```
tasks-fastapi/
├── main.py              # Punto de entrada de la aplicación
├── db.py                # Configuración de base de datos
├── .env.example         # Ejemplo de variables de entorno para la aplicación
├── .env.docker.example  # Ejemplo de variables de entorno para Docker
├── docker-compose.yaml  # Configuración Docker
├── models/              # Modelos SQLAlchemy
├── schemas/             # Esquemas Pydantic
├── repositories/        # Repositorios de datos
├── services/            # Lógica de negocio
└── routers/             # Rutas de la API
```

## Seguridad

**Importante**: Los archivos `.env` contienen credenciales sensibles y no deben ser incluidos en el control de versiones. Asegúrate de agregar `.env` a tu archivo `.gitignore`:

```bash
echo ".env" >> .gitignore
```

El proyecto incluye archivos de ejemplo como referencia:
- `.env.example` - Variables de entorno para la aplicación FastAPI
- `.env.docker.example` - Variables de entorno para Docker Compose

Estos archivos contienen las plantillas de configuración sin valores reales de producción.

