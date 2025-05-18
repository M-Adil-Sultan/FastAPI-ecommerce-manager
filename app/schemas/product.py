from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    category_id: int
    price: float
