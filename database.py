from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql+pg8000://postgres:123456@localhost:5432/inventory_db"
engine=create_engine(db_url)
session=sessionmaker(autoflush=False, autocommit=False, bind=engine)