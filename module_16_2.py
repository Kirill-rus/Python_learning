# Выполнение задания на тему "валидация данных" - "аннотация и валидация".

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()  # Инициализация.

@app.get("/")
async def welcome():
    return 'Главная страница'

@app.get("/user/admin")
async def admin_page_message():
    return 'Вы вошли как администратор'

@app.get("/user/{username}/{age}'")
async def user_info_message(username : Annotated[str , Path(min_length=5, max_length=20, description='Enter username',
                                                            example='UrbanUser')],
                            age : int = Path(ge=1, le=100, description='Enter ageD', example=24)):
    return f'Информация о пользоватaеле. Имя: {username}, Возраст: {age}'

@app.get("/user/{user_id}")
async def user_page_message(user_id : int = Path(ge=1, le=100, description='Enter User ID', example=1)):
    return f'Вы вошли как пользователь № {user_id}'