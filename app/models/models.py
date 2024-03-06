from pydantic import BaseModel, EmailStr, conint
from typing import Union


class User(BaseModel):
    name: str
    id: int


class Feedback(BaseModel):
    name: str
    message: str


class UserCreate(BaseModel):
    name: str
    email: EmailStr  # Проверка на корректный email
    age: conint(gt=0)  # Проверка на корректный возраст больше 0
    is_subscribed: Union[bool, None] = None  # Необязательный параметр, если не будет введён, примет значение None
