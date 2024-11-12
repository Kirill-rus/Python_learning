# Выполнение задания на тему "многопроцессное считывание".


# Импорт нужных библиотек:
from multiprocessing import Pool
import datetime


# Функция чтения файла построчно:
def read_info(name):
    all_data = []
    file = open(name, 'r', encoding='utf-8')

    while True:
        line = file.readline()
        all_data.append(line)

        if not line: # Остнавливается перед пустой строкой.
            break

# Объявление вызова функций из этого файла как основного (для правильной работы программы):
if __name__ == '__main__':

    file_list = [f'./file {number}.txt' for number in range(1, 5)] # Сами файлы уже есть на диске.

    start_time = datetime.datetime.now()               # Вызов чтения списка файлов последовательно.
    for file_counter in file_list:
        read_info(file_counter) # Сама функция чтения.
    finish_time = datetime.datetime.now()

    reading_time = finish_time - start_time
    print(f'На чтение файлов последовательно ушло: {reading_time}')


    start_time = datetime.datetime.now()               # Вызов чтения списка файлов параллельными процессами.
    with Pool(len(file_list)) as p:
        p.map(read_info, file_list) # Набор "бассейна" с вызванными "одновременно" функциями, по одной на файл.
    finish_time = datetime.datetime.now()

    reading_time = finish_time - start_time
    print(f'На чтение всех файлов параллельно ушло: {reading_time}')