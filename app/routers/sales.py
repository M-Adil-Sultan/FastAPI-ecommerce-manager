from fastapi import FastAPI,APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional
from backend.database import get_db
from services.sales import get_sales_summary, get_revenue_by_period, get_sales_by_filters

app = FastAPI()
sales_router = APIRouter()

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
