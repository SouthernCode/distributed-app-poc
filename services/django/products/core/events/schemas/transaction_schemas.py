from pydantic import BaseModel


class TransactionSchema(BaseModel):
    """
    Class for Transaction model
    """

    id: int = None
    user_id: int
    product_id: int
    transaction_date: str
    quantity: int
    price_per_unit: float
    total_price: float


class TransactionMessageSchema(BaseModel):
    action: str
    transaction: TransactionSchema
