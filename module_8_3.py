# Выполнение задания на тему "создание исключений" -  "некорректность":


#Классы ошибок:
class IncorrectVinNumber(Exception):   # Класс ошибки, наследуемый от "исключения".

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message





class Car:  # Класс со встроенной проверкой данных при создании экземпляра.

    def __init__(self, model, vin_number, numbers):

        self.model = model

        if self.__is_valid_vin(vin_number) == True:     # Проверка правильности данных перед записью.
            self.__vin = vin_number
        else:
            raise

        if self.__is_valid_numbers(numbers) == True:    # Проверка правильности данных перед записью.
            self.__numbers = numbers
        else:
            raise



    # Обработчики ошибок данных.
    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) == False:
            raise IncorrectVinNumber('Некорректный тип vin номер')

        if vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        return True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) == False:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

        return True



# Проверочные данные:
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')