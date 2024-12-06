# Выполнение домешнего задания на тему "Простые Юнит-Тесты" - "Проверка на выносливость".

import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):

        method = runner.Runner('method')
        for i in range(0, 10):
            method.walk()

        self.assertEqual(method.distance, 50)

    def test_run(self):

        method_2 = runner.Runner('method_2')
        for j in range(0, 10):
            method_2.run()

        self.assertEqual(method_2.distance, 100)

    def test_challenge(self):

        method_3 = runner.Runner('method_3')
        method_4 = runner.Runner('method_4')

        for k in range(0, 10):
            method_3.walk()
            method_4.run()

            self.assertNotEqual(method_3.distance, method_4.distance)

if __name__ == "__main__":
    unittest.main()