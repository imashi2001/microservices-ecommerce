from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Payment Service")

# Payment Model
class Payment(BaseModel):
    order_id: int
    amount: float
    method: str   # e.g., "card", "cash"

# In-memory database
payments = []

# Get all payments
@app.get("/payments")
def get_payments():
    return payments

# Get payment by ID
@app.get("/payments/{payment_id}")
def get_payment(payment_id: int):
    for payment in payments:
        if payment["id"] == payment_id:
            return payment
    raise HTTPException(status_code=404, detail="Payment not found")

# Create payment
@app.post("/payments")
def create_payment(payment: Payment):
    new_payment = payment.dict()
    new_payment["id"] = len(payments) + 1
    new_payment["status"] = "PAID"
    payments.append(new_payment)
    return {"message": "Payment successful", "payment": new_payment}

# Update payment status
@app.put("/payments/{payment_id}")
def update_payment(payment_id: int, status: str):
    for payment in payments:
        if payment["id"] == payment_id:
            payment["status"] = status
            return {"message": "Payment updated", "payment": payment}
    raise HTTPException(status_code=404, detail="Payment not found")

# Delete payment
@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):
    for payment in payments:
        if payment["id"] == payment_id:
            payments.remove(payment)
            return {"message": "Payment deleted"}
    raise HTTPException(status_code=404, detail="Payment not found")