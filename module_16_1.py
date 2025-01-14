# Выполнение задания на тему "основы Fast Api и маршрутизация" - "начало пути".

from fastapi import FastAPI

app = FastAPI()  # Инициализация.

@app.get("/")
async def welcome():
    return 'Главная страница'

@app.get("/user/admin")
async def admin_page_message():
    return 'Вы вошли как администратор'

@app.get("/user")
async def user_info_message(username : str = 'dummy_user', age : int = 00):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

@app.get("/user/{user_id}")
async def user_page_message(user_id : int):
    return f'Вы вошли как пользователь № {user_id}'