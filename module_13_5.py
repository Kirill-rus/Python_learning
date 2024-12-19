# Выполнение задания "клавиатура кнопок" - "меньше текста, больше кликов".

# Импорт необходимых библиотек:
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio

# Подключение к Telegram:
api = 'dummy'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())


@dp.message_handler(commands = ['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton(text='Рассчитать')
    button_2 = KeyboardButton(text='Информация')
    kb.row(button_1, button_2) # Расположение кнопок горизонтально (согласно картинке задания).
    await message.reply('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)


# Создание пользовательского класса:
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = ['Информация']) # Информация о боте.
async def bot_information(message):
    await message.answer('Информация о боте.')

@dp.message_handler(text = ['Рассчитать']) # Команда начала расчётов.
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()                      # Запись возраста.

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()                   # Запись роста.

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()                   # Запись веса.

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()                  # Создание словаря со всеми данными.
    data['calories'] = (10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5 * float(data['age'])) + 5
    await message.answer(f'Ваша норма калорий: {data["calories"]}.')
    await state.finish()                           # Завершение работы машины состояний.


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)