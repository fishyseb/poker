import unittest
from equity import straight

class TestStraightFunction(unittest.TestCase):

    def test_simple_straight(self):
        # Test a hand with a straightforward straight: 9, 10, J, Q, K
        cards = [
            {"val": 13, "suit": "H"}, {"val": 12, "suit": "S"}, {"val": 11, "suit": "C"},
            {"val": 10, "suit": "D"}, {"val": 9, "suit": "S"}
        ]
        self.assertEqual(straight(cards), 13)  # Highest card in the straight

    def test_high_card_straight(self):
        # Test a hand with an Ace-high straight: 10, J, Q, K, A
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "S"}, {"val": 12, "suit": "C"},
            {"val": 11, "suit": "D"}, {"val": 10, "suit": "S"}
        ]
        self.assertEqual(straight(cards), 14)  # Highest card in the straight

    def test_low_card_straight(self):
        # Test a hand with a 5-high straight: A, 2, 3, 4, 5
        cards = [
            {"val": 14, "suit": "H"}, {"val": 5, "suit": "S"}, {"val": 4, "suit": "C"},
            {"val": 3, "suit": "D"}, {"val": 2, "suit": "S"}
        ]
        self.assertEqual(straight(cards), 5)  # Highest card in the straight

    def test_non_straight(self):
        # Test a hand with no straight
        cards = [
            {"val": 14, "suit": "H"}, {"val": 12, "suit": "S"}, {"val": 11, "suit": "C"},
            {"val": 8, "suit": "D"}, {"val": 7, "suit": "S"}
        ]
        self.assertIsNone(straight(cards))

    def test_mixed_values(self):
        # Test a hand with cards that are close to forming a straight but do not
        cards = [
            {"val": 9, "suit": "H"}, {"val": 8, "suit": "S"}, {"val": 6, "suit": "C"},
            {"val": 5, "suit": "D"}, {"val": 3, "suit": "S"}
        ]
        self.assertIsNone(straight(cards))

if __name__ == '__main__':
    unittest.main()
