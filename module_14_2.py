# Выполнение задания на тему "выбор элементов и функции в SQL запросах" - "средний баланс пользователя".

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


   #Удаление пользователя с самым большим id (шестой записи по счёту):
   #cursor.execute('SELECT MAX(id) FROM Users')
   #max_id = cursor.fetchone()[0]

   #cursor.execute('DELETE FROM Users WHERE id = ?', (f'{max_id}',))


#Удаление пользователя id = 6:
del_id = 6

cursor.execute('DELETE FROM Users WHERE id = ?', (f'{del_id}',))

#Подсчёт количества всех пользователей:
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

#Подсчёт суммы всех балансов:
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()