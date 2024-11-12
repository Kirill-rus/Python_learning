# Выполнение задания "очереди для обмена данными между потоками" - "потоки гостей в кафе".



# Импорт нужных библиотек:
import threading
from random import randint
from queue import Queue
from time import sleep


# Стол в кафе:
class Table():

    def __init__(self, number):

        self.number = number
        self.guest = None

# Гость:
class Guest(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):

        self.waiting = randint(3, 10)
        sleep(self.waiting)


# Деятельность кафе:
class Cafe():

    def __init__(self, *tables):

        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):  # Поступление гостей.

        for client in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:  # Рассаживание гостей до окончения свободных мест.
                    table.guest = client
                    client.start()
                    print(f'{client.name} сел(a) за стол номер {table.number}')
                    seated = True
                    break
            if not seated:               # Отправка остальных в очередь.
                self.queue.put(client)
                print(f'{client.name} в очереди.')


    def discuss_guests(self): # Обслуживание столов (перепосадка за свободные).

        while not self.queue.empty():
            for taked_table in self.tables:
                if taked_table.guest is not None and taked_table.guest.is_alive() == False: # Освободившиеся столы.

                    print(f'{taked_table.guest.name} покушал(-а) и ушёл(ушла).\n'
                          f'Стол номер {taked_table.number} свободен.')

                    taked_table.guest = None

                    if self.queue.empty() == False:
                        self.new_guest = self.queue.get() # Посадка за освободившийся стол клиента из очереди.
                        taked_table.guest = self.new_guest
                        print(f'{self.new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {taked_table.number}')
                        self.new_guest.start()

                else:
                    taked_table.guest.join()
                    print(f'{taked_table.guest.name} покушал(-а) и ушёл(ушла).\n'
                          f'Стол номер {taked_table.number} свободен.')






# Проверочные данные:

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
