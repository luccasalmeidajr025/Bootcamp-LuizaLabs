from datetime import datetime, timedelta
from typing import Dict, List, Optional
import uuid

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, Field

SECRET_KEY = "change_this_to_a_random_secret_change_it"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app = FastAPI(
    title="API Bancária Assíncrona",
    description="API simples para gerenciar contas e transações (depósitos/saques) com autenticação JWT",
    version="1.0",
)


# ----------------- Schemas -----------------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=4)
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    full_name: Optional[str]


class AccountCreate(BaseModel):
    nickname: Optional[str] = None


class TransactionCreate(BaseModel):
    account_id: str
    amount: float


class TransactionOut(BaseModel):
    id: str
    type: str
    amount: float
    date: datetime


class AccountOut(BaseModel):
    id: str
    owner: str
    balance: float
    nickname: Optional[str]
    transactions: List[TransactionOut] = []


users: Dict[str, Dict] = {}
accounts: Dict[str, Dict] = {}


# ----------------- Auth -----------------
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str):
    user = users.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = users.get(token_data.username)
    if user is None:
        raise credentials_exception
    return user


# ----------------- Endpoints -----------------
@app.post("/signup", response_model=UserOut, status_code=201)
async def signup(payload: UserCreate):
    if payload.username in users:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed = get_password_hash(payload.password)
    users[payload.username] = {
        "username": payload.username,
        "full_name": payload.full_name,
        "hashed_password": hashed,
        "accounts": [],
    }
    return {"username": payload.username, "full_name": payload.full_name}


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/accounts", response_model=AccountOut, status_code=201)
async def create_account(payload: AccountCreate, current_user: Dict = Depends(get_current_user)):
    account_id = str(uuid.uuid4())
    account = {
        "id": account_id,
        "owner": current_user["username"],
        "balance": 0.0,
        "nickname": payload.nickname,
        "transactions": [],
    }
    accounts[account_id] = account
    current_user["accounts"].append(account_id)
    return AccountOut(**account)


@app.get("/accounts", response_model=List[AccountOut])
async def list_accounts(current_user: Dict = Depends(get_current_user)):
    result = [AccountOut(**accounts[a]) for a in current_user["accounts"]]
    return result


def _create_transaction_record(t_type: str, amount: float):
    return {
        "id": str(uuid.uuid4()),
        "type": t_type,
        "amount": amount,
        "date": datetime.utcnow(),
    }


@app.post("/transactions/deposit", response_model=TransactionOut)
async def deposit(payload: TransactionCreate, current_user: Dict = Depends(get_current_user)):
    if payload.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    account = accounts.get(payload.account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account["owner"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="Not authorized for this account")
    account["balance"] += payload.amount
    tr = _create_transaction_record("Deposit", payload.amount)
    account["transactions"].append(tr)
    return TransactionOut(**tr)


@app.post("/transactions/withdraw", response_model=TransactionOut)
async def withdraw(payload: TransactionCreate, current_user: Dict = Depends(get_current_user)):
    if payload.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    account = accounts.get(payload.account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account["owner"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="Not authorized for this account")
    if payload.amount > account["balance"]:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    account["balance"] -= payload.amount
    tr = _create_transaction_record("Withdraw", payload.amount)
    account["transactions"].append(tr)
    return TransactionOut(**tr)


@app.get("/accounts/{account_id}/statement", response_model=AccountOut)
async def statement(account_id: str, current_user: Dict = Depends(get_current_user)):
    account = accounts.get(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    if account["owner"] != current_user["username"]:
        raise HTTPException(status_code=403, detail="Not authorized for this account")
    return AccountOut(**account)
