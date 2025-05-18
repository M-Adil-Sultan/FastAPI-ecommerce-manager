from fastapi import FastAPI ,APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from services.demo_data import populate_db

app = FastAPI()
data_router = APIRouter()

@data_router.post("/populate-demo-data")
def populate_data_api(db: Session = Depends(get_db)):
    return populate_db(db)