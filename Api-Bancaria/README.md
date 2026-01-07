# API Bancária Assíncrona

Pequena API usando FastAPI para gerenciar contas correntes e transações (depósito/saque) com autenticação JWT.

Como rodar

1. Crie e ative um ambiente virtual (recomendado).
2. Instale dependências:

```bash
pip install -r Api-Bancaria/requirements.txt
```

3. Rode a aplicação:

```bash
uvicorn Api-Bancaria.app:app --reload
```

4. Documentação automática disponível em `http://127.0.0.1:8000/docs`.

Endpoints principais

- `POST /signup` — criar usuário
- `POST /token` — obter token (OAuth2 password grant)
- `POST /accounts` — criar conta (auth required)
- `GET /accounts` — listar contas do usuário (auth required)
- `POST /transactions/deposit` — depositar (auth required)
- `POST /transactions/withdraw` — sacar (auth required)
- `GET /accounts/{account_id}/statement` — extrato (auth required)

Observações

- Armazenamento em memória (reinicia quando a aplicação reinicia).
- Troque `SECRET_KEY` em `app.py` por uma chave segura em produção.
