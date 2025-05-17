from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from routers import __version__
from sqlalchemy.orm import Session
from sqlalchemy import text
from backend.database import get_db

app = FastAPI()
sample_router = APIRouter(prefix="/api", tags=["Version"])

@sample_router.get("/version", status_code=status.HTTP_200_OK)
def get_version():
    try:
        return {"version": __version__}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@sample_router.get("/health/db")
def test_database_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Database connected successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

app.include_router(sample_router)