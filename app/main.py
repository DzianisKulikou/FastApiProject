import uvicorn
from fastapi import FastAPI

from models.models import User, Feedback, UserCreate
from bd.bd import bd_message, bd_users

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}


# новый роут
@app.get('/custom')
def read_custom_message():
    return {"message": "This is a custom message!"}


# Модель публикации
@app.post('/Feedback')
def user_message(msg: Feedback):
    bd_message.append({"name": msg.name, "message": msg.message})
    return {"message": f"Feedback received. Thank you, {msg.name}!"}


first_user = User(name='John Doe', id=1)


@app.get('/users', response_model=User)
def user_root():
    return first_user


@app.post('/create_user', response_model=UserCreate)
def create_user(user: UserCreate):
    bd_users.append(user)
    return user


if __name__ == '__main__':
    uvicorn.run('app.main:app', host='127.0.0.1', port=8000, reload=True, workers=3)
