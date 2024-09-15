# Главный модуль задания "модули и пакеты".

# Импортируем нужные нам модули и части модулей:
from fake_math import divide as fdivide
import true_math as tm

#Запросим эти функции согласно заданию:
result1 = fdivide(69, 3)
result2 = fdivide(3, 0)
result3 = tm.divide(49, 7)
result4 = tm.divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)