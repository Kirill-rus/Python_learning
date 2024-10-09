# Выполнение домашнего задания по теме "множественное наследование"ю


class Horse:                            # Класс "лошадь".
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self):
        self.x_distance = 0  # Пройденный путь.
        self.sound = 'Frrr'  # Pвук, который издаёт лошадь.
        #super().__init__() # Орёл в цепочке наследования правее лошади, т.е. вызываем "орла" из "лошади".

    def run(self, dx):
        self.x_distance += dx



class Eagle:                           # Класс "орёл".
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self):
        self.y_distance = 0  # Высота полёта.
        self.sound = 'I train, eat, sleep, and repeat'


    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self):
        #super().__init__() # Вызываем напрямую только "лошадь".
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print (self.sound)


# Тестовые данные.
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
