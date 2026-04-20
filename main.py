from fastapi import FastAPI
from model import Product
from database import session, engine
import database_models

database_models.Base.metadata.create_all(bind=engine)

app=FastAPI()

products=[
    Product(id=1, name="Phone", description="Redmi Phone", price=149, quantity=13),
    Product(id=2, name="Tv", description="32 inch LCD Tv", price=299, quantity=6),
    Product(id=3, name="Watch", description="Smart Watch", price=99, quantity=15),
    Product(id=4, name="Earphone", description="boat earphone", price=79, quantity=20),
    Product(id=5, name="Laptop", description="Hp Laptop", price=999, quantity=5)
]

@app.get("/")
def home_practice():
    return "Welcome to home page"

@app.get("/product")

def get_product():
    db=session()
    db.query()
    return products
    

@app.get("/products/{id}")

def get_productByID(id: int):
    for product in products:
        if product.id==id:
            return product
        
    return "not fetch product"

@app.put("/products")

def update_product(id:int, product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return "product updated"
    return "Product not update"

@app.post("/products")
def create_product(product:Product):
    products.append(product)
    return product
    

@app.delete("/products")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "product deleted"
    return "product not deleted"
