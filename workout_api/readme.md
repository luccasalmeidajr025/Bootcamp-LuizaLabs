# WorkoutAPI

API de competição de crossfit (exemplo educativo) criada com FastAPI.

Como executar (local):

1. Criar um ambiente virtual e instalar dependências:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Rodar a aplicação:

```bash
uvicorn workout_api.main:app --reload
```

Endpoints principais:
- `POST /categoria` criar categoria
- `POST /centro` criar centro de treinamento
- `POST /atletas` criar atleta (cpf único — IntegrityError tratada)
- `GET /atletas` listar atletas com query params `nome` e `cpf`, resposta custom minimal e paginação `limit`/`offset` via fastapi-pagination
