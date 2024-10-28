# Выполнение задания "списковые, словарные сборки".


# Исходные списки слов:

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Первая задача:
first_result = [len(x) for x in first_strings if len(x) >= 5]

print(first_result)


# Вторая задача:
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

print(second_result)


# Третья задача:
third_result = [{x: len(x)} for x in first_strings + second_strings if not len(x) % 2]

print(third_result)