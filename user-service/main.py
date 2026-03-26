from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

app = FastAPI(title="User Service")

# Temporary in-memory database
users = [
    {"id": 1, "name": "Imashi", "email": "imashi@gmail.com"},
    {"id": 2, "name": "John", "email": "john@gmail.com"}
]

# Get all users
@app.get("/users")
def get_users():
    return users

# Get user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Create new user
@app.post("/users")
def create_user(user: User):
    new_user = user.dict()
    new_user["id"] = len(users) + 1
    users.append(new_user)
    return {"message": "User created", "user": new_user}

# Update user
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: dict):
    for user in users:
        if user["id"] == user_id:
            user.update(updated_user)
            return {"message": "User updated", "user": user}
    raise HTTPException(status_code=404, detail="User not found")

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")