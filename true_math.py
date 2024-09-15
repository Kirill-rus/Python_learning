# Модуль true_math для задания module_4_1:

from math import inf

def divide(first, second):
    if second != 0:
        result = str(first / second)
    else:
        result = inf

    return result