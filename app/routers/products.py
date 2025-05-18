from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from schemas.product import ProductCreate
from services.products import create_product

products_router = APIRouter()

@products_router.post("/products/")
def register_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        new_product = create_product(db, product.name, product.category_id, product.price)
        return {
            "message": "Product registered successfully",
            "product": {
                "id": new_product.id,
                "name": new_product.name,
                "category_id": new_product.category_id,
                "price": new_product.price
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to register product: {str(e)}")
