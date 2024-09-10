import unittest
from equity import pair

class TestPairFunction(unittest.TestCase):

    def test_simple_pair(self):
        # Test a hand with a pair of Kings (13)
        cards = [
            {"val": 13, "suit": "H"}, {"val": 13, "suit": "S"},
            {"val": 10, "suit": "C"}, {"val": 9, "suit": "D"}, {"val": 7, "suit": "S"}
        ]
        self.assertEqual(pair(cards), [13, 13, 10, 9, 7])

    def test_multiple_pairs(self):
        # Test a hand with multiple pairs (Kings and Tens), should return the highest pair (Kings)
        cards = [
            {"val": 13, "suit": "H"}, {"val": 13, "suit": "S"},
            {"val": 10, "suit": "C"}, {"val": 10, "suit": "D"}, {"val": 7, "suit": "S"}
        ]
        self.assertEqual(pair(cards), [13, 13, 10, 10, 7])

    def test_no_pair(self):
        # Test a hand with no pairs
        cards = [
            {"val": 14, "suit": "H"}, {"val": 10, "suit": "S"},
            {"val": 8, "suit": "C"}, {"val": 7, "suit": "D"}, {"val": 5, "suit": "S"}
        ]
        self.assertIsNone(pair(cards))

    def test_low_pair(self):
        # Test a hand with a low pair (Fours)
        cards = [
            {"val": 4, "suit": "H"}, {"val": 4, "suit": "S"},
            {"val": 10, "suit": "C"}, {"val": 9, "suit": "D"}, {"val": 7, "suit": "S"}
        ]
        self.assertEqual(pair(cards), [4, 4, 10, 9, 7])

    def test_kickers(self):
        # Test a hand with a pair and check if the correct kickers are returned
        cards = [
            {"val": 13, "suit": "H"}, {"val": 13, "suit": "S"},
            {"val": 10, "suit": "C"}, {"val": 9, "suit": "D"}, {"val": 8, "suit": "S"}
        ]
        self.assertEqual(pair(cards), [13, 13, 10, 9, 8])

    def test_no_kickers_needed(self):
        # Test a hand with a pair, and kickers are not needed
        cards = [
            {"val": 13, "suit": "H"}, {"val": 13, "suit": "S"},
            {"val": 10, "suit": "C"}, {"val": 9, "suit": "D"}, {"val": 8, "suit": "S"}
        ]
        self.assertEqual(pair(cards, kickers_needed=False), [13, 13])

if __name__ == '__main__':
    unittest.main()
