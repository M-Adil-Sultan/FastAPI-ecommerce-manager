from fastapi import FastAPI,APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional
from backend.database import get_db
from services.sales import get_sales_summary, get_revenue_by_period, get_sales_by_filters, create_sale
from schemas.sales import SaleCreate

app = FastAPI()
sales_router = APIRouter()

@sales_router.post("/sales/")
def add_sale(sale_data: SaleCreate, db: Session = Depends(get_db)):
    try:
        sale = create_sale(db, sale_data.store_name, sale_data.sale_date, sale_data.items)
        return {
            "message": "Sale recorded successfully",
            "sale_id": sale.id,
            "total_amount": sale.total_amount
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to record sale: {str(e)}")

@sales_router.get("/summary")
def sales_summary(db: Session = Depends(get_db)):
    return get_sales_summary(db)

@sales_router.get("/revenue")
def revenue_by_period(period: str = Query(..., enum=["daily", "weekly", "monthly", "yearly"]), db: Session = Depends(get_db)):
    return get_revenue_by_period(db, period)

@sales_router.get("/by-filters")
def sales_by_filters(
    start_date: datetime,
    end_date: datetime,
    product_id: Optional[int] = None,
    category_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    return get_sales_by_filters(db, start_date, end_date, product_id, category_id)
