# Выполнение задания на тему "создание БД, добавление, выбор и удаление элементов" - "первые пользователи".

import sqlite3

#Подколючение базы данных:
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

#Создание таблицы по условию задания:
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('''CREATE INDEX IF NOT EXISTS idx_email ON Users(email)''')

#Заполнение базы данных:
for i in range (1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'user{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

#Обновление базы данных:
for j in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, f'{j}'))
    #cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser')

#Удаление части записей:
for k in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (f'{k}',))

#Выбор части записей:
cursor.execute('SELECT username, age, balance FROM Users WHERE age <> ?', (60,))


users = cursor.fetchall()
for user in users:
    print(user)


connection.commit()
connection.close()