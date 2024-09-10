import unittest
from equity import highcard

class TestHighCard(unittest.TestCase):
    
    def test_simple_highcard(self):
        # Test with a hand where the highest card is Ace (14)
        cards = [{"val": 14, "suit": "H"}, {"val": 10, "suit": "D"}, {"val": 7, "suit": "S"}]
        self.assertEqual(highcard(cards), 14)

    def test_tie_highcard(self):
        # Test where two cards have the same high value
        cards = [{"val": 10, "suit": "H"}, {"val": 10, "suit": "D"}, {"val": 7, "suit": "S"}]
        self.assertEqual(highcard(cards), 10)

    def test_low_cards(self):
        # Test with low cards where the highest card is 8
        cards = [{"val": 4, "suit": "H"}, {"val": 8, "suit": "D"}, {"val": 2, "suit": "S"}]
        self.assertEqual(highcard(cards), 8)

    def test_mixed_suits(self):
        # Test with mixed suits where the highest card is King (13)
        cards = [{"val": 13, "suit": "H"}, {"val": 11, "suit": "C"}, {"val": 9, "suit": "S"}]
        self.assertEqual(highcard(cards), 13)

if __name__ == '__main__':
    unittest.main()
