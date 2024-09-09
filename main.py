from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import Gender, Role, User

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


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted"}
