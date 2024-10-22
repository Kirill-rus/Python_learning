# Задание по теме "Try и Except" - "программистам всё можно".

def add_everything_up(a, b):                        # Функция сложения двух переменных.
    input_type_a = ''
    inpit_type_b = ''


    try:                                         # Попытка просто сложить две переменные.
        c = a + b
        return float("{:.3f}".format(c))

    except TypeError as exc:                     # Обработка ошибки, при которой одна из переменных не число.
        if isinstance(a, (int, float)) == False:
            input_type_a = type(a)  # Сохранение "ошибочного" типа переменной.


        if isinstance(b, (int, float)) == False:
            input_type_b = type(b)

        a = str(a) # Преобразование обеих переменных в строку, чтобы обработать ошибку.
        b = str(b)

        c = a + b

        return c #, input_type_a, inpit_type_b

    #finally:
        #print('Каким был тип нечисловой переменной можно узнать, если раскомментировать вывод в ecxept.')




# Проверочные данные:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))



