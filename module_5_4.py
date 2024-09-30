#Выполнение задания "различие атрибутов класса и экземпляра".


# Создание класса "Дом":
class House:
    houses_history = [] # История созданных объектов.

    def __new__(cls, *args, **kwargs):
        #print(args)
        #print(kwargs)
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f'{self.name} снесён, но останется в истории.')

    def __init__(self, name, number_of_floors): #Описание свойств класса.
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self): #Готовый "магический" метод 1.
        return self.number_of_floors

    def __str__(self): #Готовый "магический" метод 2.
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    # Перегружаемые методы:

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)



    # Метод движения лифта:

    def go_to(self, new_floor):                 #Метод класса.
        current_floor = 1
        if new_floor not in range(1, self.number_of_floors):
            print('Такого этажа не существует.')
        else:
            while current_floor >= 1 and current_floor <= new_floor:
                print(current_floor)
                current_floor += 1



# Обращение к классу согласно заданию:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)