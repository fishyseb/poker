import unittest
from copy import deepcopy
from equity import get_winners, create_deck, get_hand_ranking

class TestGetWinners(unittest.TestCase):

    def setUp(self):
        self.players = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player2", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}]},
            {"name": "Player3", "hand": [{"val": 8, "suit": "C"}, {"val": 6, "suit": "D"}]}
        ]

    def test_basic_functionality(self):
        # Assume we have hand rankings where Player1 has the highest hand
        result = get_winners(self.players)
        self.assertEqual(result, ["Player1"])

    def test_chop_scenario(self):
        # Assume Player1 and Player2 have the same hand ranking
        players = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player2", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player3", "hand": [{"val": 8, "suit": "C"}, {"val": 6, "suit": "D"}]}
        ]
        result = get_winners(players)
        self.assertEqual(result, ["Player1", "Player2"])

    def test_no_players(self):
        players = []
        result = get_winners(players)
        self.assertEqual(result, [])

    def test_return_idx(self):
        # This test assumes that the lowest score corresponds to the best hand.
        players = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player2", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}]}
        ]
        result = get_winners(players, return_idx=True)
        self.assertIsInstance(result, int)

    def test_return_names(self):
        # Test to check if names are returned
        players = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player2", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player3", "hand": [{"val": 7, "suit": "D"}, {"val": 3, "suit": "C"}]}
        ]
        result = get_winners(players)
        self.assertEqual(result, ["Player1", "Player2"])

    def test_edge_cases(self):
        # Test when all hands are identical
        players = [
            {"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player2", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]},
            {"name": "Player3", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]}
        ]
        result = get_winners(players)
        self.assertEqual(result, ["Player1", "Player2", "Player3"])

if __name__ == "__main__":
    unittest.main()
