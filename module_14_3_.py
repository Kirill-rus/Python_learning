# Выполнение задания "доработка бота" - "витамины для всех!".

# Импорт необходимых библиотек:
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

# Подключение к Telegram:
api = 'dummy'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

# Создание inline клавиатуры:
kb_i = InlineKeyboardMarkup(resize_keyboard=True)
button_1_i = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2_i = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_i.row(button_1_i, button_2_i) # Расположение кнопок горизонтально (согласно картинке задания).

# Создание второй inline клавиатуры:
kb_i_2 = InlineKeyboardMarkup(resize_keyboard=True)
button_1_i_2 = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
button_2_i_2 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
button_3_i_2 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
button_4_i_2 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
kb_i_2.row(button_1_i_2, button_2_i_2, button_3_i_2, button_4_i_2) # Расположение кнопок горизонтально (согласно картинке задания).


@dp.message_handler(text = ['Рассчитать'])
async def main_menu(message):
    await message.reply('Выберите опцию:', reply_markup=kb_i)


@dp.callback_query_handler(text = ['formulas'])
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.message_handler(commands = ['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    kb_b = ReplyKeyboardMarkup(resize_keyboard=True) #, one_time_keyboard=True)
    button_1_b = KeyboardButton(text='Рассчитать')
    button_2_b= KeyboardButton(text='Информация')
    button_3_b = KeyboardButton(text='Купить', callback_data='buy')
    kb_b.row(button_1_b, button_2_b) # Расположение кнопок горизонтально (согласно картинке задания).
    kb_b.row(button_3_b)  # Вторая строка клавиатуры.
    await message.reply('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_b)


@dp.callback_query_handler(text = ['info'])
async def info(call):
    await call.message.answer('Информация о боте')
    await call.answer()


# Создание пользовательского класса:
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = ['Информация']) # Информация о боте.
async def bot_information(message):
    await message.answer('Информация о боте.')


@dp.callback_query_handler(text = ['calories']) # Команда начала расчётов.
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
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

@dp.message_handler(text = ['Купить']) # Вывод ассортимента продуктов с картинками.
async def get_buying_list(message):
    image_number = 1
    for product_number in range(1, 5):
        with open(f'0{image_number}.jpg', 'rb') as img:
            await message.answer(f'Название: Product{product_number} | Описание: описание {product_number} | Цена: '
                                 f'{product_number * 100}')
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup = kb_i_2)

@dp.callback_query_handler(text = ['product_buying']) # Команда покупки продукта.
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
