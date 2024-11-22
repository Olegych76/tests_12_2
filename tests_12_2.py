import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def walk(self):
        self.distance += self.speed
    
    def run(self):
        self.distance += self.speed * 2

    def __str__(self):
        return self.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[::]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    self.participants.remove(participant)
                    place += 1

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.p1, self.p2, self.p3 = Runner('Усэйн', 10), Runner('Андрей', 9), Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f'{key}: ''{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}')

    def test_start_one(self):
        t = Tournament(90, self.p1, self.p3)
        result = t.start()
        self.__class__.all_results['Тест 1'] = result
        self.assertTrue(result[max(result.keys())].name == 'Ник')

    def test_start_two(self):
        t = Tournament(90, self.p2, self.p3)
        result = t.start()
        self.__class__.all_results['Тест 2'] = result
        self.assertTrue(result[max(result.keys())].name == 'Ник')

    def test_start_three(self):
        t = Tournament(90, self.p1, self.p2, self.p3)
        result = t.start()
        self.__class__.all_results['Тест 3'] = result
        self.assertTrue(result[max(result.keys())].name == 'Ник')


if __name__ == '__main__':
    unittest.main()
