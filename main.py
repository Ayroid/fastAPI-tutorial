from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        middle_name="Smith",
        gender=Gender.male,
        roles=[Role.admin],
    ),
    User(
        id=uuid4(),
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
