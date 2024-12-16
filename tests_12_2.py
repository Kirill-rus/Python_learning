from runner_and_tournament import Tournament, Runner
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):                     # Назначение участников.

        self.first_runner = Runner('Усейн', 10)
        self.second_runner = Runner('Андрей', 9)
        self.third_runner = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):              # Вывод общей таблицы.
        for result in cls.all_results:
            print(result)


    def test_tournament(self):
        self.first_tournament = Tournament(90, self.first_runner, self.third_runner) #Условия и запуск первого турнира.
        self.first_results = self.first_tournament.start()

        #Извлечение информации для наглядного вывода результатов по участникам первого турнира:
        self.first_results_formatted = ''
        for i in range(1, len(self.first_results)+1):
            self.first_results_formatted += f'{i}: {self.first_results[i]}'
            if i != len(self.first_results):
                self.first_results_formatted +=', '

        # Добавление фигурных скобок для соответствия вывода условию задачи.
        self.first_results_formatted = '{' + self.first_results_formatted + '}'
        self.all_results.append(self.first_results_formatted) # Добавление результата в общую таблицу.


        #---------------------------------------------------------------------------------------------------------------
        self.second_tournament = Tournament(90, self.second_runner, self.third_runner) #Условия и запуск второго
        self.second_results = self.second_tournament.start()                           #турнира.


        #Извлечение информации для наглядного вывода результатов по участникам второго турнира:
        self.second_results_formatted = ''


        for i in range(1, len(self.second_results) + 1):
            self.second_results_formatted += f'{i}: {self.second_results[i]}'
            if i != len(self.second_results):
                self.second_results_formatted += ', '

        # Добавление фигурных скобок для соответствия вывода условию задачи.
        self.second_results_formatted = '{' + self.second_results_formatted + '}'
        self.all_results.append(self.second_results_formatted) # Добавление результата в общую таблицу.

        # ---------------------------------------------------------------------------------------------------------------
        self.third_tournament = Tournament(90, self.first_runner, self.second_runner, self.third_runner)
        self.third_results = self.third_tournament.start()

        # Извлечение информации для наглядного вывода результатов по участникам третьего турнира:
        self.third_results_formatted = ''
        for i in range(1, len(self.third_results) + 1):
            self.third_results_formatted += f'{i}: {self.third_results[i]}'
            if i != len(self.third_results):
                self.third_results_formatted += ', '

        # Добавление фигурных скобок для соответствия вывода условию задачи.
        self.third_results_formatted = '{' + self.third_results_formatted + '}'
        self.all_results.append(self.third_results_formatted) # Добавление результата в общую таблицу.



if __name__ == "__main__":
    unittest.main()