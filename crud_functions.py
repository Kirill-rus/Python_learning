import sqlite3

def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    );
    ''')


def add_product(product_id, title, description, price):
    chech_product = cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))

    if chech_product.fetchone() is None:
        cursor.execute(f'''
        INSERT INTO Products VALUES('{product_id}', '{title}', '{description}', '{price}')

        ''')
    connection.commit()

def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    all_data = cursor.execute('SELECT * FROM Products')
    all_data = all_data.fetchall()
    return all_data

def add_user(username, email, age):     # Добавление нового пользователя в базу.
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    is_exist = is_included(username) # Проверка на наличие пользователя в базе.

    balance = 1000 # Баланс по умолчанию.

    if is_exist == None: # Если пользователя нет - добавляем.
        new_user_id = 1 # Стартовый id пользователя.
        max_current_id = cursor.execute(f'SELECT MAX (id) FROM Users').fetchone()[0]
        if max_current_id == None: # Преобразование id пользователя в число.
            max_current_id = 1
        else:
            new_user_id = max_current_id + 1
        cursor.execute(f'''
        INSERT INTO Users VALUES('{new_user_id}', '{username}', '{email}', '{age}', '{balance}')
        ''')
    connection.commit()

def is_included(incoming_username): # Проверка на наличие пользователя в базе.
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (incoming_username,)).fetchone()
    return check_user



if __name__ == '__main__':

    # Создание базы данных, если ещё не существует:
    initiate_db()

    # Заполнение базы данных тестовыми записями:
    for id in range(1, 5):
        connection = sqlite3.connect('Products.db')
        cursor = connection.cursor()

        add_product(id, f'Продукт {id}', f'Описание {id}', f'{id*100}')
    connection.commit()

    print(get_all_products()[0])