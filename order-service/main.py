from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Order Service")

# Order Model
class Order(BaseModel):
    user_id: int
    product_id: int
    quantity: int

# In-memory database
orders = []

# Get all orders
@app.get("/orders")
def get_orders():
    return orders

# Get order by ID
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

# Create order
@app.post("/orders")
def create_order(order: Order):
    new_order = order.dict()
    new_order["id"] = len(orders) + 1
    new_order["status"] = "CREATED"
    orders.append(new_order)
    return {"message": "Order created", "order": new_order}

# Update order status
@app.put("/orders/{order_id}")
def update_order(order_id: int, status: str):
    for order in orders:
        if order["id"] == order_id:
            order["status"] = status
            return {"message": "Order updated", "order": order}
    raise HTTPException(status_code=404, detail="Order not found")

# Delete order
@app.delete("/orders/{order_id}")
def delete_order(order_id: int):
    for order in orders:
        if order["id"] == order_id:
            orders.remove(order)
            return {"message": "Order deleted"}
    raise HTTPException(status_code=404, detail="Order not found")