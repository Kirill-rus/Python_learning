# Выполнение задания на тему "блокировки и обработка ошибок" - "банковские операции".

# Импорт необходимых библиотек:
import threading
import time
from random import randint


# Создание класса:
class Bank():

    def __init__(self): # balance, lock):

        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):

        for i in range(100):
            if self.balance >= 500 and self.lock.locked():  # Разблокировка ветви при достаточности средств.
                self.lock.release()
                print ('Снятие блокировки.\n')

            self.incoming = randint(50, 500)
            self.balance += self.incoming
            print(f'Пополнение: {self.incoming}. Баланс: {self.balance}.\n')
            time.sleep(0.001)

    def take(self):

        for j in range(100):
            self.outcoming = randint(50, 500)

            print(f'Запрос на {self.outcoming}')
            if self.outcoming <= self.balance:
                self.balance -= self.outcoming
                print(f'Снятие: {self.outcoming}. Баланс: {self.balance}\n')

            else:
                print('Запрос отклонён, недостаточно средств.\n')
                #print('Установка блокировки.')
                self.lock.acquire()     # Блокировка ветви при недостаточности средств.
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

