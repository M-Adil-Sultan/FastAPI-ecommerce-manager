from backend.database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.version import sample_router
from routers.demo_data import data_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow only specific origins or use ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, you can customize it to only allow certain methods like "GET", "POST"
    allow_headers=["*"],  # Allows all headers, you can customize it
)


app.include_router(sample_router, prefix="/api", tags=["Version"])
app.include_router(data_router, prefix="/api", tags=["One time run to populate demo data"])
