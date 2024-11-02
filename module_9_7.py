# Выполнение задания на тему "декораторы".
def is_prime(func):      # Функция-декоратор, определяющая, простое ли число результат исходной функции.

    def wrapper(*args, **kwargs):

        is_prime_flag = True

        test_num = func(*args, **kwargs)

        for i in range(2, test_num - 1):
            if test_num % i == 0:
                is_prime_flag = False

        if is_prime_flag == True:
            print('Простое')
        else:
            print('Сложное')

        return test_num

    return wrapper


@is_prime
def sum_three(*args):    # Функция, складывающаяя (три) числа.
    summa = sum(args)
    return summa



# Проверочные данные:
result = sum_three(2, 3, 6)
print(result)

#result = sum_three(2, 3, 7)
#print(result)