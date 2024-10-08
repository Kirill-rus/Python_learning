# Выполнение задания "доступ к свойствам родителя. Переопределение свойств. (Изменять нельзя получать)."

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        #print(f'Модель: {self.model}')
        return f' Модель: {self.model} \n'
    def get_horsepower(self):
        #print(f'Мощность двигателя: {self.__engine_power}')
        return f'Мощность двигателя: {self.__engine_power}\n'

    def get_color(self):
        #print(f'Цвет: {self.__color}')
        return f'Цвет: {self.__color} \n'

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if str(new_color).lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
            #print(f'Цвет изменён на {new_color}.')
        else:
            print(f'Нельзя сменить цвет на {new_color}.')

class Sedan (Vehicle):
    __PASSENGERS_LIMIT = 5

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, owner, model, color, engine_power):
        super().__init__(self, owner, model, color, engine_power)


vehicle1 = Vehicle('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()