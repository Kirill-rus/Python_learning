import runner_and_tournament
import runner
import unittest

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):

        self.first_runner = runner_and_tournament.Runner('Усейн', 10)
        self.second_runner = runner_and_tournament.Runner('Андрей', 9)
        self.third_runner = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament(self):
        self.first_tournament = runner_and_tournament.Tournament(90, self.first_runner, self.third_runner)
        self.all_results[1] = [runner.name for runner in self.first_tournament.start()]

        self.second_tournament = runner_and_tournament.Tournament(90, self.second_runner, self.third_runner)
        self.all_results[2] = [runner.name for runner in self.second_tournament.start()]

        self.third_tournament = runner_and_tournament.Tournament(90, self.first_runner, self.second_runner,
                                                                 self.third_runner)
        self.all_results[3] = [runner.name for runner in self.third_tournament.start()]

        #print(list(list(self.all_results.val(self.all_results)[-1]] == self.third_runner)

        #print(self.first_runner, 'Проверка')

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):

        method = runner.Runner('method')
        for i in range(0, 10):
            method.walk()

        self.assertEqual(method.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):

        method_2 = runner.Runner('method_2')
        for j in range(0, 10):
            method_2.run()

        self.assertEqual(method_2.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):

        method_3 = runner.Runner('method_3')
        method_4 = runner.Runner('method_4')

        for k in range(0, 10):
            method_3.walk()
            method_4.run()

            self.assertNotEqual(method_3.distance, method_4.distance)

if __name__ == "__main__":
    unittest.main()