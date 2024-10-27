# Выполнение задания по теме "введение в функциональное программирование" - "вызов разом":

def apply_all_func(int_list, *functions):

    checked_list = [] # Список проверенных входных данных.

    for item in int_list: # Перевод всех пунктов входящего массива в нужный формат.

        try:
            item = int(item)
            checked_list.append(item)
        except:
            print(f'Значение "{item}" не является числом.') # Перехват ошибки, в случае если пункт списка не число.



    results = {} # Словарь, который нужно вывести по заданию.

    for function in functions:

        calculation = function(checked_list)        # Применение функции.
        results[function.__name__] = calculation    # Добавление пункта словаря.

    return results


# Проверочные данные:
print(apply_all_func([6, 20, 15, 9], max, min))
#print(apply_all_func([6, 'a', 20, [1,0], 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
