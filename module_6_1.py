# Выполнение задачи "съедобное, несъедобное" задания "зачем нужно наследование".


class Animal: # Класс "животное".
    alive: bool = True # Свойства класса.
    fed: bool = False
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name, alive :bool = True, fed :bool = True):
        self.name = name # Свойства экземпляра.
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}.')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}.')
            self.alive = False


class Plant: # Класс "растение".
    edible: bool = False # Свойства класса.
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name):
        self.name = name  # Свойства экземпляра.


class Mammal(Animal): # Подкласс "травоядное".
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)


class Predator(Animal): # Подкласс "хищник".
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)


class Flower(Plant): # Подкласс "цветок".
    pass


class Fruit(Plant): # Подкласс "фрукт".
    edible = True



# Тестовые данные:
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
