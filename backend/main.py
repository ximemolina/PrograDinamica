from fastapi import APIRouter, FastAPI
from models import *
from algorithms.series_deportivas import *

app = FastAPI()
router = APIRouter(prefix="/api")

@router.post("/series-deportivas")
async def calcular_series(entrada_series: Entradas_Series):
    return series(entrada_series.juegos, entrada_series.ph, entrada_series.pr, entrada_series.formato )

@router.get("/health")
async def health():
    return {"message": "Hola, este servicio está activo :)"}

app.include_router(router)