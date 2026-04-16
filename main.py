from fastapi import FastAPI
from model import Product
app=FastAPI()


@app.get('/')

def greet():
    return "Welcome to Our WebSite"

products=[
    Product(id=1, name="phone", description="Base model", price=199, quantity=10 ),
    Product(id=2, name="laptop", description="dell laptop", price=499, quantity=6),
    Product(id=3, name="watch", description="Dial watch", price=99, quantity=20 ),
    Product(id=4, name="Tv", description="LED Tv", price=299, quantity=3 ),
]

@app.get('/products')

def get_all_product():
    return products

@app.get('/products/{id}')

def get_product_byId(id:int):
    for product in products:
        if product.id==id:
            return product
    return "product not found"

@app.post('/product')

def create_product(product: Product):
    products.append(product)
    return product

@app.put('/product')

def update_product(id:int, product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]= product
            return "product updated successfully"
    return "No product found"

@app.delete('/product')
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "product deleted successfully"
    return "product not deleted"
        