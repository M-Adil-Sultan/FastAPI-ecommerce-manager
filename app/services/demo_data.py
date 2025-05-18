import random
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from models import Category, Product, Inventory, Sale, SaleItem

def populate_db(db: Session) -> dict:
    try:
        if db.query(Product).first():
            return {"message": "Demo data already exists. Skipping."}

        categories = [
            Category(name="Electronics", description="Devices and gadgets"),
            Category(name="Books", description="Printed and digital books"),
            Category(name="Clothing", description="Apparel for all genders")
        ]
        db.add_all(categories)
        db.commit()

        products = [
            Product(name="Smartphone", description="Android smartphone", price=699.99, category_id=1),
            Product(name="Laptop", description="Gaming laptop", price=1299.99, category_id=1),
            Product(name="Bluetooth Headphones", description="Noise-cancelling", price=199.99, category_id=1),
            Product(name="Novel Book", description="Mystery novel", price=14.99, category_id=2),
            Product(name="Science Book", description="Physics fundamentals", price=39.99, category_id=2),
            Product(name="Biography", description="Famous life story", price=24.99, category_id=2),
            Product(name="T-Shirt", description="Cotton T-shirt", price=9.99, category_id=3),
            Product(name="Jeans", description="Slim fit jeans", price=49.99, category_id=3),
            Product(name="Jacket", description="Winter jacket", price=89.99, category_id=3),
            Product(name="Sneakers", description="Running shoes", price=79.99, category_id=3),
        ]
        db.add_all(products)
        db.commit()

        inventory_items = [
            Inventory(product_id=prod.id, quantity=random.randint(20, 100))
            for prod in products
        ]
        db.add_all(inventory_items)
        db.commit()

        store_names = ["Amazon", "Walmart"]
        for _ in range(10):
            sale_date = datetime.now(timezone.utc) - timedelta(days=random.randint(0, 30))
            store = random.choice(store_names)
            num_items = random.randint(1, 4)
            chosen_products = random.sample(products, num_items)

            sale = Sale(store_name=store, sale_date=sale_date, total_amount=0.0)
            db.add(sale)
            db.commit()

            total = 0.0
            for product in chosen_products:
                quantity = random.randint(1, 3)
                item_total = float(product.price) * quantity
                total += item_total

                sale_item = SaleItem(
                    sale_id=sale.id,
                    product_id=product.id,
                    quantity=quantity,
                    unit_price=product.price
                )
                db.add(sale_item)

            sale.total_amount = total
            db.commit()

        return {"message": "✅ Demo data populated successfully."}

    except Exception as e:
        db.rollback()
        return {"error": str(e)}