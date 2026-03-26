from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Product Service")

# Product Model
class Product(BaseModel):
    name: str
    price: float
    stock: int

# In-memory database
products = [
    {"id": 1, "name": "Laptop", "price": 250000, "stock": 10},
    {"id": 2, "name": "Phone", "price": 80000, "stock": 25}
]

# Get all products
@app.get("/products")
def get_products():
    return products

# Get product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Add new product
@app.post("/products")
def create_product(product: Product):
    new_product = product.dict()
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return {"message": "Product added", "product": new_product}

# Update product
@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for product in products:
        if product["id"] == product_id:
            product.update(updated_product.dict())
            return {"message": "Product updated", "product": product}
    raise HTTPException(status_code=404, detail="Product not found")

# Delete product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")