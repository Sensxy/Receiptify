from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.receipt import Receipt

app = FastAPI(title="Receipt Analyzer", version="1.0.0")

@app.get("/")
async def read_root():
    return {"message": "Receipt Analyzer API is running!"}

@app.get("/receipts")
async def get_receipts(db: Session = Depends(get_db)):
    receipts = db.query(Receipt).all()
    return {"receipts": receipts, "count": len(receipts)}

@app.post("/receipts/test")
async def create_test_receipt(db: Session = Depends(get_db)):
    test_receipt = Receipt(
        merchant_name="Test Store",
        amount=25.99,
        category="Food & Dining",
        status="completed"
    )
    db.add(test_receipt)
    db.commit()
    return {"message": "Test receipt created!"}