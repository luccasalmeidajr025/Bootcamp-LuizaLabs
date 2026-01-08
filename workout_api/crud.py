from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas


def create_categoria(db: Session, payload: schemas.CategoriaCreate):
    obj = models.Categoria(nome=payload.nome)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def create_centro(db: Session, payload: schemas.CentroCreate):
    obj = models.CentroTreinamento(nome=payload.nome, endereco=payload.endereco, proprietario=payload.proprietario)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def create_atleta(db: Session, payload: schemas.AtletaCreate):
    obj = models.Atleta(
        nome=payload.nome,
        cpf=payload.cpf,
        idade=payload.idade,
        peso=payload.peso,
        altura=payload.altura,
        sexo=payload.sexo,
        centro_treinamento_id=payload.centro_treinamento_id,
        categoria_id=payload.categoria_id,
    )
    db.add(obj)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise
    db.refresh(obj)
    return obj


def get_atletas(db: Session, nome: str = None, cpf: str = None):
    q = db.query(models.Atleta)
    if nome:
        q = q.filter(models.Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        q = q.filter(models.Atleta.cpf == cpf)
    return q.order_by(models.Atleta.nome).all()
