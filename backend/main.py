from fastapi import APIRouter, FastAPI
from models import *
from algorithms.series_deportivas import *
from algorithms.reemplazo import *

app = FastAPI()
router = APIRouter(prefix="/api")

# PROYECTO 01
@router.post("/reemplazo-equipos")
async def calcular_reemplazos(entrada_reemplazos: Entradas_Reemplazos):
    periodos = [p.model_dump() for p in entrada_reemplazos.periodos] # no usar objeto Periodos, transformarlo en dict
    return reemplazo(entrada_reemplazos.costoInicial, entrada_reemplazos.plazo, entrada_reemplazos.vidaUtil,periodos )

# PROYECTO 02
@router.post("/series-deportivas")
async def calcular_series(entrada_series: Entradas_Series):
    return series(entrada_series.juegos, entrada_series.ph, entrada_series.pr, entrada_series.formato )

@router.get("/health")
async def health():
    return {"message": "Hola, este servicio está activo :)"}

app.include_router(router)