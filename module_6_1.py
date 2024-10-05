# Выполнение задачи "съедобное, несъедобное" задания "зачем нужно наследование".


class Animal: # Класс "животное".
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name, alive :bool = True, fed :bool = True):
        self.name = name
        self.alive = alive
        self.fed = fed



class Plant: # Класс "растение".
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name, edible: bool = False):
        self.name = name
        self.edible = edible



class Mammal(Animal): # Подкласс "травоядное".
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}.')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}.')
            self.alive = False


class Predator(Animal): # Подкласс "хищник".
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}.')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}.')
            self.alive = False

class Flower(Plant): # Класс "цветок".
    pass


class Fruit(Plant): # Класс "фрукт".
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
