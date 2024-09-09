from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        # This generates a random UUID
        # id=uuid4(),
        # To fix the id use
        id=UUID("123e4567-e89b-12d3-a456-426614174000"),
        first_name="John",
        last_name="Doe",
        middle_name="Smith",
        gender=Gender.male,
        roles=[Role.admin],
    ),
    User(
        id=UUID("123e4567-e89b-12d3-a456-426614174001"),
        first_name="Not",
        last_name="Doe",
        middle_name="John",
        gender=Gender.other,
        roles=[Role.user],
    ),
]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    user.id = uuid4()
    db.append(user)
    return user


@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_update: UserUpdateRequest):
    for user in db:
        if user.id == user_id:
            user.first_name = user_update.first_name
            user.last_name = user_update.last_name
            user.middle_name = user_update.middle_name
            user.roles = user_update.roles
            return user
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")
