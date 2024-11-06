# Выполнение задания "введение в потоки" - "потоковая запись в файлы".

import time              # Импорт нужных библиотек.
import threading

def write_words(word_count, file_name):                # Основная функция для параллельных действий.

    #global finish_time_u
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i+1}\n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    #finish_time_u = time.time()



# Проверочные данные:

start_time_s = time.time()            # Время начала последовательной записи.
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_time_s = time.time()           # Время завершения последовательной записи.

work_time = finish_time_s - start_time_s  # Вычисление продолжительности работы.
#print('Время работы', work_time)

# Форматирование строки согласно условию:
time_in_format = str(time.strftime('%H:%M:%S', time.gmtime(work_time))) + str(round(work_time - int(work_time), 5))[1:]
print(f'Работа потоков {time_in_format}')




start_time_p = time.time()           # Время начала параллельной записи.
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_1.start()
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_2.start()
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_3.start()
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
finish_time_p = time.time()          # Время завершения параллельной записи.

work_time = finish_time_p - start_time_p

time_in_format = str(time.strftime('%H:%M:%S', time.gmtime(work_time))) + str(round(work_time - int(work_time), 5))[1:]
print(f'Работа потоков {time_in_format}')
