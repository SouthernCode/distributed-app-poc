from pydantic import BaseModel
from datetime import datetime


class TransactionBase(BaseModel):
    """
    Base class for Transaction model
    Used by pydantic to validate the model
    And by fastapi to validate request bodies and return responses
    """

    user_id: int
    product_id: int
    transaction_date: datetime = datetime.now()
    quantity: int
    price_per_unit: float
    total_price: float

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "product_id": 1,
                "transaction_date": "2018-01-05T16:59:33+00:00",
                "quantity": 1,
                "price_per_unit": 1.0,
                "total_price": 1.0,
            }
        }


class TransactionCreate(TransactionBase):
    """
    Class for Transaction creation
    """

    user_id: int = None
    pass


class Transaction(TransactionBase):
    """
    Class for Transaction model
    """

    id: int = None

    class Config:
        orm_mode = True


class TransactionMessage(BaseModel):
    """
    Class for Transaction message to be
    sent to the message broker
    """

    action: str
    transaction: Transaction
