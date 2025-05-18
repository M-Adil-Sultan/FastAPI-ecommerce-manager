from pydantic import BaseModel
from typing import List

class SaleItemInput(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

class SaleCreate(BaseModel):
    store_name: str
    sale_date: str  # ISO format, e.g., "2024-05-17T13:00:00Z"
    items: List[SaleItemInput]
