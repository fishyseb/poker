import unittest
from equity import full_house  # Replace `poker_game` with the actual module name where your function is

class TestFullHouseFunction(unittest.TestCase):

    def test_simple_full_house(self):
        # Test a hand with a clear full house
        cards = [
            {"val": 14, "suit": "H"}, {"val": 14, "suit": "D"}, {"val": 14, "suit": "C"},
            {"val": 10, "suit": "S"}, {"val": 10, "suit": "H"}
        ]
        self.assertEqual(full_house(cards), [14, 14, 14, 10, 10])

    def test_no_full_house(self):
        # Test a hand that does not form a full house
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "D"}, {"val": 12, "suit": "C"},
            {"val": 11, "suit": "S"}, {"val": 10, "suit": "H"}
        ]
        self.assertIsNone(full_house(cards))

    def test_full_house_with_extra_cards(self):
        # Test a hand with extra cards that do not affect the full house
        cards = [
            {"val": 14, "suit": "H"}, {"val": 14, "suit": "D"}, {"val": 14, "suit": "C"},
            {"val": 10, "suit": "S"}, {"val": 10, "suit": "H"}, {"val": 9, "suit": "D"},
            {"val": 8, "suit": "C"}
        ]
        self.assertEqual(full_house(cards), [14, 14, 14, 10, 10])

    def test_edge_case_with_multiple_full_houses(self):
        # Test a hand where two potential full houses are possible
        cards = [
            {"val": 14, "suit": "H"}, {"val": 14, "suit": "D"}, {"val": 14, "suit": "C"},
            {"val": 10, "suit": "S"}, {"val": 10, "suit": "H"}, {"val": 9, "suit": "D"},
            {"val": 9, "suit": "C"}
        ]
        # The function should return the best full house, which is the one with 14s and 10s
        self.assertEqual(full_house(cards), [14, 14, 14, 10, 10])

if __name__ == '__main__':
    unittest.main()
