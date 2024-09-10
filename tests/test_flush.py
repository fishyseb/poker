import unittest
from equity import flush

class TestFlushFunction(unittest.TestCase):

    def test_simple_flush(self):
        # Test a hand with exactly five cards of the same suit
        cards = [
            {"val": 14, "suit": "H"}, {"val": 12, "suit": "H"}, {"val": 11, "suit": "H"},
            {"val": 10, "suit": "H"}, {"val": 9, "suit": "H"}
        ]
        self.assertEqual(flush(cards), [14, 12, 11, 10, 9])  # Should return the top 5 cards

    def test_flush_with_more_than_five_cards(self):
        # Test a hand with more than five cards of the same suit; should return top 5 cards
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "H"}, {"val": 12, "suit": "H"},
            {"val": 11, "suit": "H"}, {"val": 10, "suit": "H"}, {"val": 9, "suit": "H"}
        ]
        self.assertEqual(flush(cards), [14, 13, 12, 11, 10])

    def test_no_flush(self):
        # Test a hand with no flush
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "S"}, {"val": 12, "suit": "D"},
            {"val": 11, "suit": "C"}, {"val": 10, "suit": "S"}
        ]
        self.assertIsNone(flush(cards))

    def test_flush_with_return_all_suited(self):
        # Test a hand with more than five cards of the same suit and return_all_suited=True
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "H"}, {"val": 12, "suit": "H"},
            {"val": 11, "suit": "H"}, {"val": 10, "suit": "H"}, {"val": 9, "suit": "H"}
        ]
        self.assertEqual(flush(cards, return_all_suited=True), [14, 13, 12, 11, 10, 9])


if __name__ == '__main__':
    unittest.main()
