from typing import Optional
from pydantic import BaseModel


class CategoriaCreate(BaseModel):
    nome: str


class CentroCreate(BaseModel):
    nome: str
    endereco: Optional[str] = None
    proprietario: Optional[str] = None


class AtletaCreate(BaseModel):
    nome: str
    cpf: str
    idade: Optional[int] = None
    peso: Optional[float] = None
    altura: Optional[float] = None
    sexo: Optional[str] = None
    centro_treinamento_id: Optional[str] = None
    categoria_id: Optional[str] = None


class AtletaOutMinimal(BaseModel):
    nome: str
    centro_treinamento: Optional[str] = None
    categoria: Optional[str] = None

    class Config:
        orm_mode = True
