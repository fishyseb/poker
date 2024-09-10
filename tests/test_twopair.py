import unittest
from equity import twopair

class TestTwoPairFunction(unittest.TestCase):

    def test_simple_two_pair(self):
        # Test a hand with exactly two pairs: Queens and Tens
        cards = [
            {"val": 12, "suit": "H"}, {"val": 12, "suit": "S"},  # Queens
            {"val": 10, "suit": "C"}, {"val": 10, "suit": "D"},  # Tens
            {"val": 8, "suit": "S"}
        ]
        self.assertEqual(twopair(cards), [12, 12, 10, 10, 8])

    def test_multiple_two_pair(self):
        # Test a hand with multiple two-pair possibilities
        cards = [
            {"val": 12, "suit": "H"}, {"val": 12, "suit": "S"},  # Queens
            {"val": 10, "suit": "C"}, {"val": 10, "suit": "D"},  # Tens
            {"val": 8, "suit": "S"}, {"val": 8, "suit": "D"}   # Eights
        ]
        self.assertEqual(twopair(cards), [12, 12, 10, 10, 8])

    def test_one_pair_only(self):
        # Test a hand with only one pair
        cards = [
            {"val": 12, "suit": "H"}, {"val": 12, "suit": "S"},  # Queens
            {"val": 10, "suit": "C"}, {"val": 9, "suit": "D"}, {"val": 8, "suit": "S"}
        ]
        self.assertIsNone(twopair(cards))

    def test_no_pairs(self):
        # Test a hand with no pairs
        cards = [
            {"val": 14, "suit": "H"}, {"val": 10, "suit": "S"},
            {"val": 8, "suit": "C"}, {"val": 7, "suit": "D"}, {"val": 5, "suit": "S"}
        ]
        self.assertIsNone(twopair(cards))

    def test_two_pair_with_kickers(self):
        # Test a hand with two pairs and multiple kickers
        cards = [
            {"val": 12, "suit": "H"}, {"val": 12, "suit": "S"},  # Queens
            {"val": 10, "suit": "C"}, {"val": 10, "suit": "D"},  # Tens
            {"val": 8, "suit": "S"}, {"val": 7, "suit": "D"}   # Kickers
        ]
        self.assertEqual(twopair(cards), [12, 12, 10, 10, 8])

    def test_no_kickers_needed(self):
        # Test a hand with two pairs and no kickers needed
        cards = [
            {"val": 12, "suit": "H"}, {"val": 12, "suit": "S"},  # Queens
            {"val": 10, "suit": "C"}, {"val": 10, "suit": "D"},  # Tens
            {"val": 8, "suit": "S"}, {"val": 7, "suit": "D"}
        ]
        self.assertEqual(twopair(cards, kickers_needed=False), [12, 12, 10, 10])

if __name__ == '__main__':
    unittest.main()
