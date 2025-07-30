from app.database.database import engine, Base
from app.models.receipt import Receipt, User

# Create all tables
Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")
