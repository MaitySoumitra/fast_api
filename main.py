from fastapi import FastAPI, Depends
from model import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session
database_models.Base.metadata.create_all(bind=engine)

app=FastAPI()

products=[
    Product(id=1, name="Phone", description="Redmi Phone", price=149, quantity=13),
    Product(id=2, name="Tv", description="32 inch LCD Tv", price=299, quantity=6),
    Product(id=3, name="Watch", description="Smart Watch", price=99, quantity=15),
    Product(id=4, name="Earphone", description="boat earphone", price=79, quantity=20),
    Product(id=5, name="Laptop", description="Hp Laptop", price=999, quantity=5)
]

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db=session()
    count=db.query(database_models.Product).count()

    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
            db.commit()
init_db()

@app.get("/")
def home_practice():
    return "Welcome to home page"



@app.get("/product")

def get_product(db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).all()
    return db_products
    

@app.get("/products/{id}")

def get_productByID(id:int, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product
        
    return "not product found"

@app.put("/products")

def update_product(id:int, product:Product, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return "Product updated"
    else:
        return "Product not update"

@app.post("/products")
def create_product(product:Product, db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product
    

@app.delete("/products")
def delete_product(id:int, db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted"
    else:
        return "product not deleted"
