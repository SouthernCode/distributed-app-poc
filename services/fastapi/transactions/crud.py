from sqlalchemy.orm import Session

from models.TransactionModel import TransactionModel
from schemas import transaction_schemas


def get_transaction(db: Session, transaction_id: int):
    """
    Get transaction by id
    """
    return (
        db.query(TransactionModel).filter(TransactionModel.id == transaction_id).first()
    )


def get_transactions(
    db: Session, skip: int = 0, limit: int = 100, user_id: int = None
) -> list:
    """
    Get all transactions
    """
    if user_id:
        return (
            db.query(TransactionModel)
            .filter(TransactionModel.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    return db.query(TransactionModel).offset(skip).limit(limit).all()


def create_transaction(
    db: Session, transaction: transaction_schemas.TransactionCreate
) -> TransactionModel:
    """
    Create new transaction
    """
    db_transaction = TransactionModel(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
