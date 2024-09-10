import unittest
from equity import quads  # Replace `poker_game` with the actual module name where your function is

class TestQuadsFunction(unittest.TestCase):

    def test_simple_quads(self):
        # Test a hand with a clear four of a kind
        cards = [
            {"val": 14, "suit": "H"}, {"val": 14, "suit": "D"}, {"val": 14, "suit": "C"},
            {"val": 14, "suit": "S"}, {"val": 10, "suit": "H"}
        ]
        self.assertEqual(quads(cards), [14, 14, 14, 14, 10])

    def test_no_quads(self):
        # Test a hand that does not form quads
        cards = [
            {"val": 14, "suit": "H"}, {"val": 13, "suit": "D"}, {"val": 12, "suit": "C"},
            {"val": 11, "suit": "S"}, {"val": 10, "suit": "H"}
        ]
        self.assertIsNone(quads(cards))

    def test_quads_with_extra_cards(self):
        # Test a hand with extra cards that do not affect the quads
        cards = [
            {"val": 14, "suit": "H"}, {"val": 14, "suit": "D"}, {"val": 14, "suit": "C"},
            {"val": 14, "suit": "S"}, {"val": 10, "suit": "H"}, {"val": 9, "suit": "D"},
            {"val": 8, "suit": "C"}
        ]
        self.assertEqual(quads(cards), [14, 14, 14, 14, 10])

    def test_edge_case_with_multiple_quads(self):
        # Test a hand where multiple quads are possible but only the best one should be returned
        cards = [
            {"val": 14, "suit": "H"}, {"val": 14, "suit": "D"}, {"val": 14, "suit": "C"},
            {"val": 14, "suit": "S"}, {"val": 10, "suit": "H"}, {"val": 10, "suit": "D"},
            {"val": 10, "suit": "C"}
        ]
        # The function should return the highest quads, which is the one with 14s
        self.assertEqual(quads(cards), [14, 14, 14, 14, 10])

if __name__ == '__main__':
    unittest.main()
