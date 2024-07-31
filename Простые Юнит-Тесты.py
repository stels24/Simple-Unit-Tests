from Runner import Runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        wal = Runner("Mikhal")
        for i in range(10):
            wal.walk()
        self.assertEqual(wal.distance, 50)

    def test_run(self):
        run = Runner("Hasan")
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        wal = Runner("Mikhal")
        ru = Runner("Hasan")
        for i in range(10):
            wal.walk()
            ru.run()
        self.assertNotEqual(wal.distance, ru.distance)

if __name__ == '__main__':
    unittest.main()