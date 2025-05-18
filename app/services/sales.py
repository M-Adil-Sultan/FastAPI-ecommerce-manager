from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Sale, SaleItem, Product

def create_sale(db: Session, store_name: str, sale_date: str, items: list):
    total_amount = sum(item.quantity * item.unit_price for item in items)

    sale = Sale(
        store_name=store_name,
        sale_date=datetime.fromisoformat(sale_date),
        total_amount=total_amount
    )
    db.add(sale)
    db.commit()
    db.refresh(sale)

    for item in items:
        sale_item = SaleItem(
            sale_id=sale.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=item.unit_price
        )
        db.add(sale_item)

    db.commit()
    return sale

def get_sales_summary(db: Session):
    total_sales = db.query(func.count(Sale.id)).scalar()
    total_revenue = db.query(func.sum(Sale.total_amount)).scalar()
    return {
        "total_sales": total_sales,
        "total_revenue": total_revenue or 0.0
    }

def get_revenue_by_period(db: Session, period: str):
    now = datetime.now(timezone.utc)
    if period == "daily":
        start_date = now - timedelta(days=1)
    elif period == "weekly":
        start_date = now - timedelta(weeks=1)
    elif period == "monthly":
        start_date = now - timedelta(days=30)
    elif period == "yearly":
        start_date = now - timedelta(days=365)
    else:
        return {"error": "Invalid period"}

    revenue = db.query(func.sum(Sale.total_amount)).filter(Sale.sale_date >= start_date).scalar()
    return {
        "period": period,
        "revenue": revenue or 0.0
    }

def get_sales_by_filters(db: Session, start_date: datetime, end_date: datetime, product_id: int = None, category_id: int = None):
    query = db.query(Sale).filter(Sale.sale_date.between(start_date, end_date))

    if product_id:
        query = query.join(SaleItem).filter(SaleItem.product_id == product_id)

    if category_id:
        query = query.join(SaleItem).join(Product).filter(Product.category_id == category_id)

    sales = query.distinct().all()

    result = []
    for sale in sales:
        sale_info = {
            "id": sale.id,
            "store": sale.store_name,
            "date": sale.sale_date,
            "total": sale.total_amount,
            "items": []
        }

        for item in sale.items:
            if product_id and item.product_id != product_id:
                continue
            if category_id and item.product.category_id != category_id:
                continue

            sale_info["items"].append({
                "product_id": item.product_id,
                "product_name": item.product.name,
                "quantity": item.quantity,
                "unit_price": item.unit_price,
                "subtotal": item.quantity * item.unit_price
            })

        result.append(sale_info)

    return result
