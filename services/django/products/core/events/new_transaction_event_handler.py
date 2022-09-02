from core.models import Product
from core.events.schemas.transaction_schemas import TransactionSchema


def handle_new_transaction(transaction: TransactionSchema):
    """
    Handle new transaction event
    Will modify the quantity of the product based on the transaction information
    """
    print("Handling new transaction event")
    quantity = transaction.quantity
    product_id = transaction.product_id
    print(f"Will modify product {product_id} quantity by subtracting {quantity}")
    product = Product.objects.get(id=product_id)
    print(f"Current product quantity is {product.quantity}")
    new_quantity = product.quantity - quantity
    if new_quantity > 0:
        product.quantity = new_quantity
        product.save()
    else:
        raise Exception(f"Not enough quantity")  # TODO: return an error to the queue?
    print("Transaction handled successfully")
    print(f"Product quantity is now {product.quantity}")
