import unittest
import matchstick


class TestCohost(unittest.TestCase):
    def test_optimal_move(self):
        self.assertEqual(1, matchstick.optimal(2))
        self.assertEqual(2, matchstick.optimal(3))
        self.assertEqual(3, matchstick.optimal(4))

        self.assertEqual(1, matchstick.optimal(6))
        self.assertEqual(2, matchstick.optimal(7))
        self.assertEqual(3, matchstick.optimal(8))

    def test_something(self):
        self.assertEqual(None, list(matchstick.generate(7)))
