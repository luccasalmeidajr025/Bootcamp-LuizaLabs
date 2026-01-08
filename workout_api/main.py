from fastapi import FastAPI, Depends, HTTPException, status
from fastapi_pagination import add_pagination, paginate, LimitOffsetPage, Params
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from . import models, schemas, crud
from .database import SessionLocal, init_db

app = FastAPI(title="WorkoutAPI - Crossfit Competition")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    init_db()


@app.post("/categoria", status_code=201)
def create_categoria(payload: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.create_categoria(db, payload)


@app.post("/centro", status_code=201)
def create_centro(payload: schemas.CentroCreate, db: Session = Depends(get_db)):
    return crud.create_centro(db, payload)


@app.post("/atletas", status_code=201)
def create_atleta(payload: schemas.AtletaCreate, db: Session = Depends(get_db)):
    try:
        obj = crud.create_atleta(db, payload)
        return obj
    except IntegrityError as e:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {payload.cpf}")


@app.get("/atletas", response_model=LimitOffsetPage[schemas.AtletaOutMinimal])
def list_atletas(nome: str = None, cpf: str = None, params: Params = Depends(), db: Session = Depends(get_db)):
    items = crud.get_atletas(db, nome=nome, cpf=cpf)

    out = []
    for a in items:
        ct_name = a.centro_treinamento.nome if a.centro_treinamento else None
        cat_name = a.categoria.nome if a.categoria else None
        out.append(schemas.AtletaOutMinimal(nome=a.nome, centro_treinamento=ct_name, categoria=cat_name))
    return paginate(out, params)


add_pagination(app)
