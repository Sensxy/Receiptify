from sqlalchemy import Column, Integer, String, Numeric, Date, DateTime, Text
from sqlalchemy.sql import func
from app.database.database import Base

class Receipt(Base):
    __tablename__ = "receipts"
    
    id = Column(Integer, primary_key=True, index=True)
    merchant_name = Column(String, nullable=True)
    amount = Column(Numeric(10, 2), nullable=True)
    date = Column(Date, nullable=True)
    category = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    raw_ocr_text = Column(Text, nullable=True)
    status = Column(String, default="processing")  # processing, completed, failed
    created_at = Column(DateTime, default=func.now())

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=func.now())
