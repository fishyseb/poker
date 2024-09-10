import unittest
from equity import straight_flush  # Replace `poker_game` with the actual module name where your function is

class TestStraightFlushFunction(unittest.TestCase):

    def test_simple_straight_flush(self):
        # Test a hand with a clear straight flush
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "H"}, {"val": 12, "suit": "H"},
            {"val": 11, "suit": "H"}, {"val": 10, "suit": "H"}
        ]
        self.assertEqual(straight_flush(cards), 14)  # Highest card in the straight flush

    def test_no_straight_flush(self):
        # Test a hand that does not form a straight flush
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "D"}, {"val": 12, "suit": "C"},
            {"val": 11, "suit": "S"}, {"val": 10, "suit": "H"}
        ]
        self.assertIsNone(straight_flush(cards))

    def test_straight_flush_with_extra_cards(self):
        # Test a hand with extra cards that do not affect the straight flush
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "H"}, {"val": 12, "suit": "H"},
            {"val": 11, "suit": "H"}, {"val": 10, "suit": "H"}, {"val": 9, "suit": "D"},
            {"val": 8, "suit": "C"}
        ]
        self.assertEqual(straight_flush(cards), 14)  # Highest card in the straight flush

    def test_straight_flush_with_ace_low(self):
        # Test a hand where the straight flush has an Ace as the low card
        cards = [
            {"val": 5, "suit": "H"}, {"val": 4, "suit": "H"}, {"val": 3, "suit": "H"},
            {"val": 2, "suit": "H"}, {"val": 1, "suit": "H"}
        ]
        self.assertEqual(straight_flush(cards), 5)  # Highest card in the straight flush (Ace is low)

if __name__ == '__main__':
    unittest.main()
