#Выполнение задания на тему "сложные моменты и исключения в стеке вызовов функции" - "план перехват":

def personal_sum(numbers):   # Вычисление суммы чисел.
    result = 0
    incorrect_data = 0
    #print(len(numbers))

    try:
        for i in numbers:
            try:
                result += i
            except TypeError as exc_1:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
    except TypeError as exc_1:
        incorrect_data += 1
        result = None

    return result, incorrect_data

def calculate_average(numbers):  # Вычисление среднего арифметического чисел.

    collection_data = personal_sum(numbers)
    total_sum = collection_data[0]
    total_count = 0

    #print('\nВсего элементов нечислового типа в массиве.', collection_data[1])

    try:
        total_count = len(numbers) - collection_data[1]
    except TypeError as exc_2:
        #print('\nДля обработки передана не коллекция.')
        pass

    try:
        average = total_sum / total_count
        return average
    except ZeroDivisionError as exc_2:
        #print('\nЧисел в переданном массиве (коллекции) не обнаружено.')
        return 0
    except TypeError as exc_2:
        print('В numbers записан некорректный тип данных.')
        return None



# Проверочные данные:
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать