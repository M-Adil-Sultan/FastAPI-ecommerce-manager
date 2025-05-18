from sqlalchemy import Column, Integer, DECIMAL, String, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from backend.database import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    store_name = Column(String(100))
    sale_date = Column(DateTime, default=datetime.now(timezone.utc))
    total_amount = Column(DECIMAL(10, 2))

    items = relationship("SaleItem", back_populates="sale")
