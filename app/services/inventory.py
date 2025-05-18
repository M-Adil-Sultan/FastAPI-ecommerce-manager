from sqlalchemy.orm import Session
from models import Inventory, Product

LOW_STOCK_THRESHOLD = 10

def get_inventory_status(db: Session, low_stock_only: bool = False):
    query = db.query(Inventory).join(Product)

    if low_stock_only:
        query = query.filter(Inventory.quantity <= LOW_STOCK_THRESHOLD)

    inventory_list = query.all()

    return [
        {
            "product_id": item.product.id,
            "product_name": item.product.name,
            "quantity": item.quantity,
            "low_stock": item.quantity <= LOW_STOCK_THRESHOLD
        }
        for item in inventory_list
    ]

def update_inventory_level(db: Session, product_id: int, new_quantity: int):
    inventory = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    if not inventory:
        return {"error": "Inventory not found for product"}

    inventory.quantity = new_quantity
    db.commit()
    db.refresh(inventory)

    return {
        "message": "Inventory updated successfully",
        "product_id": inventory.product_id,
        "new_quantity": inventory.quantity
    }