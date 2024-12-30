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