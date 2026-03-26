from fastapi import FastAPI
import requests

app = FastAPI(title="API Gateway")

# USER SERVICE
@app.get("/users")
def get_users():
    return requests.get("http://localhost:8001/users").json()

# PRODUCT SERVICE
@app.get("/products")
def get_products():
    return requests.get("http://localhost:8002/products").json()

# ORDER SERVICE
@app.get("/orders")
def get_orders():
    return requests.get("http://localhost:8003/orders").json()

# PAYMENT SERVICE
@app.get("/payments")
def get_payments():
    return requests.get("http://localhost:8004/payments").json()