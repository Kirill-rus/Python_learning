# Выполнение задания "генераторные сборки".


# Исходные данные:
first = ['Strings', 'Student', 'Computers']
#second = ['Строка', 'Урбан']
second = ['Строка', 'Урбан', 'Компьютер']



try:
    if len(first) != len(second):           # Проверка одинаковости длин списков.
        print('Длины входных списков не равны. Выводятся данные только по первым сравнённым словам.')


    lists_combination = zip(first, second)  # Cборка массива их пар строк, находящихся на одинаковых местах в списке.
    first_result = [] # Создание списка разностей длин срок.

    for i in lists_combination:             # Поиск разности длин строк, находящхся на одном и том же месте в списке.
        if len(i[0]) != len(i[1]):
            first_result.append(abs(len(i[0]) - len(i[1])))

except IndexError as exc_1:
    print(f'Ошибка {exc_1}. Выводятся данные только по первым сравнённым словам.')


print(first_result)




try:
    second_result = [] # Создание списка совпедений длин срок.

    for i in range(len(first)):
        if len(first[i]) != len(second[i]):
            second_result.append(False)
        else:
            second_result.append(True)

except IndexError as exc_2:
    print(f'Ошибка "{exc_2}". Выводятся данные только по первым сравнённым словам.')

print(second_result)


