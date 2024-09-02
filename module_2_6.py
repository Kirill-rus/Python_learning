key_input = int(input('Введите целое число, для которого надо найти слагаемые: '))

# Проверим ввод на условия задачи:
if key_input < 3:
    key_input = 3

if key_input > 20:
    key_input = 20


key_iteration_massive = []

print('Все пары слагаемых:')
for i in range(0, (key_input//2)): # Чтобы исключить большинство дубликатов в парах проходим только по половине чисел.
    for j in range(0, key_input):
        if key_input % (i+1 + j+1) == 0: # Если пара - делитель исходного числа, то добавляем в массив.
            print (f'{key_input} = {i+1} + {j+1}')
            key_iteration_massive.append(i+1)
            key_iteration_massive.append(j+1)

print('Полный массив слагаемых:', key_iteration_massive)


# Упорядочим в парах слагаемые так, чтобы они шли по возрастанию:
for sistematization in range(0, (len(key_iteration_massive)-2), 2):
   if key_iteration_massive[sistematization] > key_iteration_massive[sistematization + 1]:
       temp_var = key_iteration_massive[sistematization]
       key_iteration_massive[sistematization] = key_iteration_massive[sistematization + 1]
       key_iteration_massive[sistematization + 1] = temp_var

print('Массив слагаемых с упорядоченными парами:', key_iteration_massive)

# Удалим все дубликаты (заменим на нули):
for check in range(0, (len(key_iteration_massive)-3), 2):  # Проход по левым частям для сравнения.
   left_sum = key_iteration_massive[check] + key_iteration_massive[check + 1] # Первый делитель исходного числа.

   for check_2 in range(check + 2, (len(key_iteration_massive) - 1), 2): # Проход по правым частям для сравнения.
       right_sum = key_iteration_massive[check_2] + key_iteration_massive[check_2 + 1] #Второй делитель исходного числа.

       if left_sum == right_sum and right_sum != key_input: # Если пары равны - обнуляем их.
           if key_iteration_massive[check] == key_iteration_massive[check_2]:
               key_iteration_massive[check_2] = 0
               key_iteration_massive[check_2 + 1] = 0
       else:
           continue

print('Массив с обнулёнными дубликатами:', key_iteration_massive)

#Удалим нули из массива:
key_iteration_massive = [element for element in key_iteration_massive if element != 0]

#Получим требуемое значение:
print('Массив, очищенный от нулей, заменявших дубликаты:', key_iteration_massive)