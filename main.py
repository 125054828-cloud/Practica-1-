"""Inventario de red — Práctica 3.

Alumno: Fatima Anel Martinez Montero
Matrícula: 125054828
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Inventario de red")


class Dispositivo(BaseModel):
    nombre: str
    tipo: str
    ip: str
    activo: bool = True


class DispositivoParcial(BaseModel):
    nombre: str | None = None
    tipo: str | None = None
    ip: str | None = None
    activo: bool | None = None


inventario = [
    Dispositivo(nombre="R1", tipo="router", ip="10.0.0.1"),
    Dispositivo(nombre="SW1", tipo="switch", ip="10.0.0.10", activo=False),
    Dispositivo(nombre="FW1", tipo="firewall", ip="10.0.0.254"),
]
def buscar(nombre: str) -> Dispositivo | None:
    """Devuelve el equipo con ese nombre, o None si no existe."""
    for equipo in inventario:
        if equipo.nombre.upper() == nombre.upper():
            return equipo
    return None

@app.get("/")
async def estado():
    """Comprueba que el servicio responde."""
    return {"servicio": "Inventario de red", "total": len(inventario)}

@app.get("/dispositivos")
async def listar(activo: bool | None = None):
    """Lista el inventario. Con ?activo=true filtra los que están en línea."""
    if activo is None:
        return inventario
    return [equipo for equipo in inventario if equipo.activo == activo]
@app.get("/dispositivos/{nombre}")
async def obtener(nombre: str):
    """Busca un equipo por su nombre."""
    equipo = buscar(nombre)
    if equipo is None:
        raise HTTPException(status_code=404,
                            detail=f"No existe el equipo {nombre}")
    return equipo

@app.put("/dispositivos/{nombre}")
async def reemplazar(nombre: str, datos: Dispositivo):
    """Sustituye por completo el registro de un equipo."""
    equipo = buscar(nombre)
    if equipo is None:
        raise HTTPException(status_code=404,
                            detail=f"No existe el equipo {nombre}")
    inventario[inventario.index(equipo)] = datos
    return datos


@app.patch("/dispositivos/{nombre}")
async def modificar(nombre: str, cambios: DispositivoParcial):
    """Modifica solo los campos enviados."""
    equipo = buscar(nombre)
    if equipo is None:
        raise HTTPException(status_code=404,
                            detail=f"No existe el equipo {nombre}")
    for campo, valor in cambios.model_dump(exclude_unset=True).items():
        setattr(equipo, campo, valor)
    return equipo