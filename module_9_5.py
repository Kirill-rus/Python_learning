# Выполнение домашнего задания по теме "итераторы" - "range - это просто".

class StepValueError(ValueError):   # Класс обработки ошибки.
    pass


class Iterator:                              # Класс итератора.

    def __init__(self, start, stop, step=1):

        self.start = start
        self.stop = stop

        if step == 0:                        # Проверка правильности шага.
            raise StepValueError('шаг не может быть равен 0')
        else:
            self.step = step

        self.first_call = True     # Метка первого шага.


    def __iter__(self):

        self.pointer = self.start  # Установка начального значения указателя.
        return self


    def __next__(self):

        if self.first_call:                     # Действия на первом шаге.

            self.first_call = False # Изменение метки первого шага.

            if self.step > 0  and self.start > self.stop:             # Проверка правильности направления итерирования.
                raise StopIteration('Неверное направление итерирования.')
            if self.step < 0 and self.start < self.stop:
                raise StopIteration('Неверное направление итерирования.')

            return self.pointer            # Возврат итерируемого значения.



        self.pointer = self.pointer + self.step # Действия при последующих шагах.


        if self.step > 0:                 # Выяснение направления пересчёта (+/-).
            if self.pointer >= self.stop:
                raise StopIteration
        if self.step < 0:
            if self.pointer <= self.stop:
                raise StopIteration

        return self.pointer               # Возврат итерируемого значения.





# Проверочные данные:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')


iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)      #


for i in iter2:
    print(i, end=' ')
print()


for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()


for i in iter5:
    print(i, end=' ')
print()
