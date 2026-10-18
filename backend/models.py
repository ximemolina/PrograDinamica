from pydantic import BaseModel

class Entradas_Series(BaseModel):
    algoritmo: str="series-deportivas"
    juegos: int
    ph: float
    pr: float
    formato: list[bool]

class Periodo(BaseModel):
    reventa: float     
    mantenimiento: float 

class Entradas_Reemplazos(BaseModel):
    algoritmo: str="reemplazo-equipos"
    costoInicial: float
    plazo: int
    vidaUtil: int
    periodos: list[Periodo]
