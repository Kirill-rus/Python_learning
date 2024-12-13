# Выполнение домашнего задания на тему "логирование бегунов".

from runner_12_4 import Runner
import unittest
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат записи
    handlers=[
        logging.FileHandler('runner_tests.log', mode='w', encoding='utf-8'),  # Обработчик для записи в файл
        logging.StreamHandler()  # Обработчик для вывода в консоль
    ]
)


class RunnerTest(unittest.TestCase):

    #is_frozen = False

    #@unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:

            runner_1 = Runner('runner_1', -10)
            for i in range(0, 10):
                runner_1.walk()

            self.assertEqual(runner_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner')

    #@unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:

            runner_2 = Runner('runner_2', some_variable)
            for j in range(0, 10):
                runner_2.run()

            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner')


    #@unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):

        runner_3 = Runner('runner_3')
        runner_4 = Runner('runner_4')

        for k in range(0, 10):
            runner_3.walk()
            runner_4.run()

            self.assertNotEqual(runner_3.distance, runner_4.distance)

if __name__ == "__main__":
    unittest.main()
