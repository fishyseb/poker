import unittest
from copy import deepcopy

from equity import create_final_hands

class TestCreateFinalHands(unittest.TestCase):

    def test_basic_functionality(self):
        players = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player2", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}]}
        ]
        final_board = [{"val": 2, "suit": "C"}, {"val": 9, "suit": "H"}]

        expected = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}, {"val": 2, "suit": "C"}, {"val": 9, "suit": "H"}]},
            {"name": "Player2", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}, {"val": 2, "suit": "C"}, {"val": 9, "suit": "H"}]}
        ]

        result = create_final_hands(players, final_board)
        self.assertEqual(result, expected)

    def test_empty_board(self):
        players = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player2", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}]}
        ]
        final_board = []

        expected = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player2", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}]}
        ]

        result = create_final_hands(players, final_board)
        self.assertEqual(result, expected)

    def test_no_players(self):
        players = []
        final_board = [{"val": 2, "suit": "C"}, {"val": 9, "suit": "H"}]

        expected = []

        result = create_final_hands(players, final_board)
        self.assertEqual(result, expected)

    def test_large_board(self):
        players = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player2", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}]}
        ]
        final_board = [{"val": i, "suit": "C"} for i in range(1, 14)]  # Full set of 13 cards

        expected = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}] + [{"val": i, "suit": "C"} for i in range(1, 14)]},
            {"name": "Player2", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}] + [{"val": i, "suit": "C"} for i in range(1, 14)]}
        ]

        result = create_final_hands(players, final_board)
        self.assertEqual(result, expected)

    def test_cards_already_in_hand(self):
        players = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}, {"val": 2, "suit": "C"}]},
            {"name": "Player2", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}, {"val": 9, "suit": "H"}]}
        ]
        final_board = [{"val": 2, "suit": "C"}, {"val": 9, "suit": "H"}]

        expected = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}, {"val": 2, "suit": "C"}, {"val": 2, "suit": "C"}, {"val": 9, "suit": "H"}]},
            {"name": "Player2", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}, {"val": 9, "suit": "H"}, {"val": 2, "suit": "C"}, {"val": 9, "suit": "H"}]}
        ]

        result = create_final_hands(players, final_board)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
