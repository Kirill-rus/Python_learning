# Выполнение домашнего задания на тему "логирование бегунов".

import runner_12_4
import unittest
import logging


class RunnerTest(unittest.TestCase):

    #is_frozen = False

    #@unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    try:
        def test_walk(self):

            method = runner_12_4.Runner('method', -10)
            for i in range(0, 10):
                method.walk()

            self.assertEqual(method.distance, 50)
            logging.info('"test_walk" выполнен успешно')
    except:
        logging.warning('Неверная скорость для Runner')

    #@unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    try:
        def test_run(self):

            method_2 = runner_12_4.Runner('method_2', some_variable)
            for j in range(0, 10):
                method_2.run()

            self.assertEqual(method_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
    except:
        logging.warning('Неверный тип данных для объекта Runner')


    #@unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):

        method_3 = runner_12_4.Runner('method_3')
        method_4 = runner_12_4.Runner('method_4')

        for k in range(0, 10):
            method_3.walk()
            method_4.run()

            self.assertNotEqual(method_3.distance, method_4.distance)

if __name__ == "__main__":
    unittest.main()
    logging.basicConfig(
        level=logging.DEBUG,  # Уровень логирования
        format='%(asctime)s - %(levelname)s - %(message)s',  # Формат записи
        handlers=[
            logging.FileHandler('runner_tests.txt', mode='w', encoding='utf-8'),  # Обработчик для записи в файл
            logging.StreamHandler()  # Обработчик для вывода в консоль
        ]
    )
