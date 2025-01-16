# Выполнение задания на тему "CRUD Запросы: Get, Post, Put Delete" - "имитация работы с БД".

from fastapi import FastAPI, Path

app = FastAPI()  # Инициализация.

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def welcome():
    return 'Главная страница'

@app.get("/users")
async def get_all_users():
    return users


@app.post("/user/{username}/{age}") # Добавление нового пользователя.
async def add_new_user(username: str = Path(min_length=5, max_length=20, description='Enter username',
                                                            example='UrbanUser'),
                       age : int = Path(ge=1, le=150, description='Enter user age', example=1)) -> str:

    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registered.'





@app.put("/user/{user_id}/{username}/{age}") # Изменение существующего пользователя.
async def edit_user(user_id, username : str = Path(min_length=5, max_length=20, description='Enter username',
                                                            example='UrbanUser'),
                    age : int = Path(ge=1, le=150, description='Enter user age', example=1)) -> str:

    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'



@app.delete("/user/{user_id}") # Удаление пользователя.
async def delete_user(user_id):
    users.pop(user_id)
    return f'User {user_id} has been deleted'

