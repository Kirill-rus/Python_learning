# Выполнение задания на тему "потоки на классах" - "за честь и отвагу!".

import threading  # Импорт нужных библиотек.
import time

class Knight(threading.Thread):           # Создание дочернего класса от ветви.
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100


    def fighting(self):                  # Создания "механизма" битвы.
        self.days = 0

        while self.enemies:
            time.sleep(1)
            self.enemies -= self.power
            self.days += 1
            print(f'{self.name} сражается {self.days} дней, осталось {self.enemies} воинов.')

        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


    def run(self):                      # Переопределение run().
        print(f'{self.name}, на нас напали!')
        self.fighting()


# Проверочные данные.
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()
print('Все битвы закончились!')