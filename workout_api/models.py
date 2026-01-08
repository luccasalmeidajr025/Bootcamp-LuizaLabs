import uuid
from sqlalchemy import Column, String, Integer, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .database import Base


def gen_uuid():
    return str(uuid.uuid4())


class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(String, primary_key=True, default=gen_uuid)
    nome = Column(String(50), unique=True, nullable=False)


class CentroTreinamento(Base):
    __tablename__ = "centro_treinamento"
    id = Column(String, primary_key=True, default=gen_uuid)
    nome = Column(String(100), unique=True, nullable=False)
    endereco = Column(String(200))
    proprietario = Column(String(100))


class Atleta(Base):
    __tablename__ = "atleta"
    id = Column(String, primary_key=True, default=gen_uuid)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(20), nullable=False, unique=True)
    idade = Column(Integer)
    peso = Column(Float)
    altura = Column(Float)
    sexo = Column(String(1))
    centro_treinamento_id = Column(String, ForeignKey("centro_treinamento.id"))
    categoria_id = Column(String, ForeignKey("categoria.id"))

    centro_treinamento = relationship("CentroTreinamento")
    categoria = relationship("Categoria")
