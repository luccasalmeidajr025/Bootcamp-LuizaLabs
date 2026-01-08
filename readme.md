# 🚀 Bootcamp LuizaLabs

Repositório com todos os projetos e exercícios desenvolvidos durante o **Bootcamp LuizaLabs**. Este bootcamp abrange fundamentos de Python, programação orientada a objetos, desenvolvimento de APIs REST e boas práticas de desenvolvimento.

---

## 📋 Índice

- [Sobre o Bootcamp](#sobre-o-bootcamp)
- [Projetos](#projetos)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Requisitos](#requisitos)
- [Como Começar](#como-começar)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuindo](#contribuindo)

---

## 📚 Sobre o Bootcamp

O **Bootcamp LuizaLabs** é um programa intensivo de desenvolvimento que combina teoria e prática para preparar desenvolvedores Python. Os projetos contemplam desde conceitos fundamentais até aplicações web com FastAPI.

### Objetivos de Aprendizado

- ✅ Dominar os fundamentos de Python
- ✅ Aplicar Programação Orientada a Objetos (POO)
- ✅ Desenvolver APIs REST com FastAPI
- ✅ Gerenciar bases de dados
- ✅ Implementar autenticação e segurança
- ✅ Seguir boas práticas de código

---

## 📂 Projetos

### 1. 🏦 Sistema Bancário em Python
**Localização:** `sistema-bancario/`

Sistema bancário básico implementado em Python puro, focando em fundamentos da linguagem.

**Funcionalidades:**
- Depósito e saque
- Extrato bancário
- Cadastro de usuários
- Cadastro de contas bancárias
- Validações de operações

**Conceitos Práticos:**
- Funções e keyword-only arguments
- Estruturas de controle
- Dicionários e listas
- Validação de dados

**Como executar:**
```bash
python sistema-bancario/desafio.py
```

---

### 2. 🏗️ Sistema Bancário com POO
**Localização:** `sistema-bancario-poo/`

Evolução do sistema bancário implementado com **Programação Orientada a Objetos**, aplicando conceitos avançados de Python.

**Funcionalidades:**
- Classes base e herança
- Histórico de transações
- Múltiplas contas por usuário
- Sistema de depósitos e saques
- Extrato com histórico completo

**Conceitos Práticos:**
- Classes abstratas e herança
- Encapsulamento
- Polimorfismo
- Tratamento de exceções
- Design Patterns

**Como executar:**
```bash
python sistema-bancario-poo/desafio.py
```

---

### 3. 🔌 API Bancária Assíncrona
**Localização:** `Api-Bancaria/`

API REST moderna desenvolvida com **FastAPI**, implementando autenticação JWT e gerenciamento de contas bancárias.

**Funcionalidades:**
- Autenticação com OAuth2 e JWT
- Criar contas correntes
- Realizar depósitos e saques
- Gerar extratos
- Sistema de usuários

**Endpoints Principais:**
- `POST /signup` — Criar usuário
- `POST /token` — Obter token de autenticação
- `POST /accounts` — Criar conta (autenticado)
- `GET /accounts` — Listar contas do usuário
- `POST /transactions/deposit` — Realizar depósito
- `POST /transactions/withdraw` — Realizar saque
- `GET /accounts/{account_id}/statement` — Obter extrato

**Conceitos Práticos:**
- REST API com FastAPI
- Autenticação e autorização
- Validação de dados
- Documentação automática (Swagger)

**Como executar:**
```bash
pip install -r Api-Bancaria/requirements.txt
uvicorn Api-Bancaria.app:app --reload
```

Acesse a documentação em: `http://127.0.0.1:8000/docs`

---

### 4. 🏋️ WorkoutAPI
**Localização:** `workout_api/`

API de competição de crossfit desenvolvida com **FastAPI**, demonstrando operações CRUD, paginação e tratamento de erros.

**Funcionalidades:**
- Gerenciar categorias de competição
- Cadastrar centros de treinamento
- Gerenciar atletas com validações
- Consultar atletas por nome ou CPF
- Paginação de resultados

**Endpoints Principais:**
- `POST /categoria` — Criar categoria
- `POST /centro` — Criar centro de treinamento
- `POST /atletas` — Criar atleta
- `GET /atletas` — Listar atletas (com filtros e paginação)

**Conceitos Práticos:**
- CRUD com FastAPI
- Validação de CPF (unicidade)
- Query parameters e paginação
- Tratamento de IntegrityError
- Respostas customizadas

**Como executar:**
```bash
pip install -r workout_api/requirements.txt
uvicorn workout_api.main:app --reload
```

---

### 5. 📝 Exercícios Python - Resolvendo Códigos
**Localização:** `resolvendo-codigos-py-copilot/`

Coleção de exercícios práticos para fortalecer fundamentos de Python e lógica de programação.

**Exercícios Inclusos:**
- `concat_dados.py` — Concatenação de strings e dados
- `media.py` — Cálculo de média
- `num_par_impar.py` — Classificar números pares e ímpares
- `ope_mat.py` — Operações matemáticas
- `palindromos.py` — Validar palíndromos
- `repet_txt.py` — Repetição de textos

**Conceitos Práticos:**
- Fundamentos de Python
- Estruturas de dados (listas, dicionários)
- Funções
- Manipulação de strings
- Lógica de programação

**Como executar:**
```bash
python resolvendo-codigos-py-copilot/nome_do_arquivo.py
```

---

## 📁 Estrutura do Repositório

```
Bootcamp-LuizaLabs/
│
├── readme.md                          # Este arquivo
│
├── sistema-bancario/                  # Sistema bancário básico
│   ├── desafio.py
│   └── readme.md
│
├── sistema-bancario-poo/              # Sistema bancário com POO
│   └── desafio.py
│
├── Api-Bancaria/                      # API bancária com FastAPI
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
├── workout_api/                       # API de crossfit
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── requirements.txt
│   └── readme.md
│
└── resolvendo-codigos-py-copilot/     # Exercícios práticos
    ├── concat_dados.py
    ├── media.py
    ├── num_par_impar.py
    ├── ope_mat.py
    ├── palindromos.py
    ├── repet_txt.py
    └── readme.md
```

---

## 🔧 Requisitos

### Geral
- **Python 3.8+**
- **pip** (gerenciador de pacotes)

### Para APIs (FastAPI)
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **SQLAlchemy** (para banco de dados)

### Para Bancos de Dados
- **SQLite** (incluído no Python) ou **PostgreSQL**

---

## 🚀 Como Começar

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/Bootcamp-LuizaLabs.git
cd Bootcamp-LuizaLabs
```

### 2. Crie um Ambiente Virtual
```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências
```bash
# Para rodar todos os projetos
pip install fastapi uvicorn pydantic sqlalchemy psycopg2-binary fastapi-pagination python-multipart python-jose cryptography

# Ou instale projeto por projeto conforme seu interesse
pip install -r Api-Bancaria/requirements.txt
pip install -r workout_api/requirements.txt
```

### 4. Execute um Projeto
```bash
# Exemplo: Sistema bancário simples
python sistema-bancario/desafio.py

# Exemplo: API Bancária
uvicorn Api-Bancaria.app:app --reload

# Exemplo: WorkoutAPI
uvicorn workout_api.main:app --reload
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso | Versão |
|-----------|-----|--------|
| **Python** | Linguagem principal | 3.8+ |
| **FastAPI** | Framework para APIs REST | Latest |
| **Uvicorn** | Servidor ASGI | Latest |
| **Pydantic** | Validação de dados | Latest |
| **SQLAlchemy** | ORM para bancos de dados | Latest |
| **SQLite/PostgreSQL** | Bancos de dados | - |
| **JWT** | Autenticação segura | - |

---

## 💡 Boas Práticas Implementadas

✅ **Validação de dados** — Usando Pydantic  
✅ **Tratamento de erros** — Com mensagens claras  
✅ **Autenticação segura** — OAuth2 com JWT  
✅ **Documentação automática** — Swagger/OpenAPI  
✅ **Separação de responsabilidades** — Modelos, schemas, CRUD  
✅ **Paginação** — Limitando resultados  
✅ **Código limpo** — Seguindo PEP 8  

---

## 📖 Documentação Adicional

Cada projeto possui um `readme.md` ou `README.md` específico com detalhes técnicos. Consulte-os para informações mais aprofundadas sobre cada projeto.

---

## 🤝 Contribuindo

Se deseja sugerir melhorias ou reportar problemas:

1. Abra uma **Issue** descrevendo o problema ou sugestão
2. Faça um **Fork** do repositório
3. Crie uma **Branch** para sua feature (`git checkout -b feature/melhoria`)
4. Commit suas mudanças (`git commit -m 'Adiciona melhoria'`)
5. Push para a branch (`git push origin feature/melhoria`)
6. Abra um **Pull Request**

---

## 📧 Contato e Suporte

- **GitHub:** [seu-perfil](https://github.com/luccasalmeidajr025)
- **LinkedIn:** [seu-perfil](linkedin.com/in/lucas-almeida-jr/)


---

## 🎓 Créditos

Desenvolvido como parte do **Bootcamp LuizaLabs**.

> *Última atualização: Janeiro de 2026*
