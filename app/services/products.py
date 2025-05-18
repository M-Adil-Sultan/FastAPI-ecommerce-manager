from sqlalchemy.orm import Session
from models import Product, Inventory

def create_product(db: Session, name: str, category_id: int, price: float):
    new_product = Product(name=name, category_id=category_id, price=price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    inventory = Inventory(product_id=new_product.id, quantity=0)
    db.add(inventory)
    db.commit()

    return new_product
