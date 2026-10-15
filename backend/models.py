from pydantic import BaseModel


class Entradas_Series(BaseModel):
    algoritmo: str="series-deportivas"
    juegos: int
    ph: float
    pr: float
    formato: list[bool]