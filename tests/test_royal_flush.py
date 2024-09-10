import unittest
from equity import royal_flush  # Replace `poker_game` with the actual module name where your function is

class TestRoyalFlushFunction(unittest.TestCase):

    def test_simple_royal_flush(self):
        # Test a hand with a clear royal flush
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "H"}, {"val": 12, "suit": "H"},
            {"val": 11, "suit": "H"}, {"val": 10, "suit": "H"}
        ]
        self.assertEqual(royal_flush(cards), 14)  # Highest card in the royal flush (Ace)

    def test_no_royal_flush(self):
        # Test a hand that does not form a royal flush
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "H"}, {"val": 12, "suit": "H"},
            {"val": 11, "suit": "H"}, {"val": 9, "suit": "H"}
        ]
        self.assertIsNone(royal_flush(cards))  # Not a royal flush

    def test_straight_flush_without_royal_flush(self):
        # Test a hand that forms a straight flush but not a royal flush
        cards = [
            {"val": 9, "suit": "H"}, {"val": 8, "suit": "H"}, {"val": 7, "suit": "H"},
            {"val": 6, "suit": "H"}, {"val": 5, "suit": "H"}
        ]
        self.assertIsNone(royal_flush(cards))  # A straight flush but not a royal flush

if __name__ == '__main__':
    unittest.main()
