from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from models.TransactionModel import TransactionModel
from schemas import transaction_schemas
from auth import AuthHandler
from database import SessionLocal, engine
import crud
from sqlalchemy.orm import Session

from broker import Broker

message_broker = Broker()


TransactionModel.metadata.create_all(bind=engine)


auth_handler = AuthHandler()

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/transactions/", response_model=list[transaction_schemas.Transaction])
async def get_transactions(
    user=Depends(auth_handler.auth_wrapper),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    user_id = user.id
    transactions = crud.get_transactions(db, skip=skip, limit=limit, user_id=user_id)
    return transactions


@app.get(
    "/api/transactions/{transaction_id}", response_model=transaction_schemas.Transaction
)
async def get_transaction(
    user=Depends(auth_handler.auth_wrapper),
    transaction_id: int = 1,
    db: Session = Depends(get_db),
):
    transaction = crud.get_transaction(db, transaction_id=transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@app.post("/api/transactions/", response_model=transaction_schemas.Transaction)
async def create_transaction(
    transaction: transaction_schemas.TransactionCreate,
    user=Depends(auth_handler.auth_wrapper),
    db: Session = Depends(get_db),
):
    user_id = user.id
    transaction.user_id = user_id
    created_transaction = crud.create_transaction(db=db, transaction=transaction)
    transaction_response = transaction_schemas.Transaction(
        **created_transaction.__dict__
    )
    message_broker.publish(
        "transaction", f"created a transaction with: {transaction_response.json()}"
    )

    return created_transaction
