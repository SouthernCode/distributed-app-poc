from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base


class TransactionModel(Base):
    """
    Transaction Model used by sqlalchemy
    """

    __tablename__ = "Transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    product_id = Column(Integer, index=True)
    transaction_date = Column(DateTime)
    quantity = Column(Integer)
    price_per_unit = Column(Float)
    total_price = Column(Float)
