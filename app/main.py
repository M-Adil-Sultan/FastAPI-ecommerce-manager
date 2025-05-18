from backend.database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.version import sample_router
from routers.demo_data import data_router
from routers.sales import sales_router
from routers.inventory import inventory_router
from routers.products import products_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)


app.include_router(sample_router, prefix="/api", tags=["Version"])
app.include_router(products_router, prefix="/api", tags=["Products"])
app.include_router(sales_router, prefix="/api", tags=["Sales"])
app.include_router(inventory_router, prefix="/api", tags=["Inventory"])
app.include_router(data_router, prefix="/api", tags=["One time run to populate demo data"])
