# Выполнение задания на тему "рекурсия".


# Функция, перемножающая цифры из последовательности на входе:
def get_multiplied_digits (number):
    str_number = str(number)
    if str_number[-1] == '0': # Исправление обнуления произведения, если в конце числа на входе стоит "0".
        str_number = str_number.rstrip('0')

    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


# Пробный запуск с серией чисел из задания:
result = get_multiplied_digits(40203) # Ошибку при прописанном вводе, начиная с "0" (040203), победить не удалось.
print('Результат при вводе из условия задачи =', result)


# Перемножение произвольного количества чисел на входе:
external_input = 'none'
while external_input != 'end':
    external_input = input('Введите последовательность однозначных чисел для перемножения (или введите "end"): ')
    if external_input.lower().find('end') >=0:
        print('Ввод остановлен.')
        break

    result_external = result = get_multiplied_digits(int(external_input))
    print('Result with external input =', result_external)

