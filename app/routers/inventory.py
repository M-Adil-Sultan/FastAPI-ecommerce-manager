from fastapi import FastAPI, APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.database import get_db
from services.inventory import get_inventory_status, update_inventory_level

app = FastAPI()
inventory_router = APIRouter()

@inventory_router.get("/status")
def inventory_status(
    low_stock_only: bool = Query(False),
    db: Session = Depends(get_db)
):
    return get_inventory_status(db, low_stock_only)

@inventory_router.put("/update/{product_id}")
def update_inventory(
    product_id: int,
    new_quantity: int = Query(..., gt=0),
    db: Session = Depends(get_db)
):
    return update_inventory_level(db, product_id, new_quantity)
