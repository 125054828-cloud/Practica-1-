# Inventario de red

API con FastAPI para consultar un inventario de dispositivos de red.

**Alumno:** Fatima Anel Martinez Montero
**Matrícula:** 125054828

## Instalación

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt

## Ejecución

    fastapi dev main.py

La documentación interactiva queda en http://127.0.0.1:8000/docs

## Rutas

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | / | Estado del servicio |
| GET | /dispositivos | Lista el inventario (acepta ?activo=true) |
| GET | /dispositivos/{nombre} | Busca un equipo por nombre |