import unittest
from equity import trips

class TestTripsFunction(unittest.TestCase):

    def test_simple_trips(self):
        # Test a hand with exactly three of a kind: Kings
        cards = [
            {"val": 13, "suit": "H"}, {"val": 13, "suit": "S"}, {"val": 13, "suit": "C"},  # Kings
            {"val": 10, "suit": "D"}, {"val": 7, "suit": "S"}
        ]
        self.assertEqual(trips(cards), [13, 13, 13, 10, 7])

    def test_multiple_trips(self):
        # Test a hand with multiple possible trips; should return the highest
        cards = [
            {"val": 13, "suit": "H"}, {"val": 13, "suit": "S"}, {"val": 13, "suit": "C"},  # Kings
            {"val": 12, "suit": "D"}, {"val": 12, "suit": "S"}, {"val": 12, "suit": "H"}   # Queens
        ]
        self.assertEqual(trips(cards), [13, 13, 13, 12, 12])

    def test_two_pair(self):
        # Test a hand with two pairs and no trips
        cards = [
            {"val": 12, "suit": "H"}, {"val": 12, "suit": "S"},  # Queens
            {"val": 10, "suit": "C"}, {"val": 10, "suit": "D"},  # Tens
            {"val": 8, "suit": "S"}
        ]
        self.assertIsNone(trips(cards))

    def test_one_pair(self):
        # Test a hand with only one pair and no trips
        cards = [
            {"val": 12, "suit": "H"}, {"val": 12, "suit": "S"},  # Queens
            {"val": 10, "suit": "C"}, {"val": 9, "suit": "D"}, {"val": 8, "suit": "S"}
        ]
        self.assertIsNone(trips(cards))

    def test_no_trips(self):
        # Test a hand with no trips
        cards = [
            {"val": 14, "suit": "H"}, {"val": 10, "suit": "S"},
            {"val": 8, "suit": "C"}, {"val": 7, "suit": "D"}, {"val": 5, "suit": "S"}
        ]
        self.assertIsNone(trips(cards))

    def test_trips_with_kickers(self):
        # Test a hand with trips and additional kickers
        cards = [
            {"val": 13, "suit": "H"}, {"val": 13, "suit": "S"}, {"val": 13, "suit": "C"},  # Kings
            {"val": 10, "suit": "D"}, {"val": 8, "suit": "S"}
        ]
        self.assertEqual(trips(cards), [13, 13, 13, 10, 8])

    def test_no_kickers_needed(self):
        # Test a hand with trips and no kickers needed
        cards = [
            {"val": 13, "suit": "H"}, {"val": 13, "suit": "S"}, {"val": 13, "suit": "C"},  # Kings
            {"val": 10, "suit": "D"}, {"val": 8, "suit": "S"}
        ]
        self.assertEqual(trips(cards, kickers_needed=False), [13, 13, 13])

if __name__ == '__main__':
    unittest.main()
