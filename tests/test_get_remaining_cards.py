import unittest
from equity import get_remaining_cards, DuplicateCardError

class TestGetRemainingCards(unittest.TestCase):

    def setUp(self):
        # Define a standard deck of cards
        self.full_deck = [
            {"val": val, "suit": suit} for val in range(2, 15) for suit in ['S', 'H', 'D', 'C']
        ]
    
    def test_basic(self):
        players = [{"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]}]
        board = [{"val": 2, "suit": "C"}, {"val": 7, "suit": "D"}]
        expected_remaining = [
            {"val": val, "suit": suit} for val in range(2, 15) for suit in ['S', 'H', 'D', 'C']
            if not (val == 10 and suit == 'H') and not (val == 5 and suit == 'S')
            and not (val == 2 and suit == 'C') and not (val == 7 and suit == 'D')
        ]
        result = get_remaining_cards(players, board)
        sorted_result = sorted(result, key=lambda x: (x['val'], x['suit']))
        sorted_expected = sorted(expected_remaining, key=lambda x: (x['val'], x['suit']))
        self.assertEqual(sorted_result, sorted_expected)
    
    def test_no_cards_in_play(self):
        players = []
        board = []
        expected_remaining = self.full_deck
        result = get_remaining_cards(players, board)
        sorted_result = sorted(result, key=lambda x: (x['val'], x['suit']))
        sorted_expected = sorted(expected_remaining, key=lambda x: (x['val'], x['suit']))
        self.assertEqual(sorted_result, sorted_expected)
    
    def test_all_cards_in_play(self):
        players = [{"name": "Player1", "hand": self.full_deck}]
        board = self.full_deck
        expected_remaining = []
        result = get_remaining_cards(players, board)
        sorted_result = sorted(result, key=lambda x: (x['val'], x['suit']))
        sorted_expected = sorted(expected_remaining, key=lambda x: (x['val'], x['suit']))
        self.assertEqual(sorted_result, sorted_expected)
    
    def test_return_used(self):
        players = [{"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]}]
        board = [{"val": 2, "suit": "C"}, {"val": 7, "suit": "D"}]
        expected_used = [
            {"val": 10, "suit": "H"}, {"val": 5, "suit": "S"},
            {"val": 2, "suit": "C"}, {"val": 7, "suit": "D"}
        ]
        result = get_remaining_cards(players, board, return_used=True)
        sorted_result = sorted(result, key=lambda x: (x['val'], x['suit']))
        sorted_expected = sorted(expected_used, key=lambda x: (x['val'], x['suit']))
        self.assertEqual(sorted_result, sorted_expected)
        
    # def test_duplicate_cards_detection(self):
    #     players = [{"name": "Player1", "hand": [{"val": 10, "suit": "H"}, {"val": 5, "suit": "S"}]}]
    #     board = [{"val": 2, "suit": "C"}, {"val": 7, "suit": "D"}]
        
    #     # Add a duplicate card to the board for testing
    #     duplicate_card = {'val': 10, 'suit': 'H'}
    #     board_with_duplicate = board + [duplicate_card]
        
    #     # Test for DuplicateCardError
    #     self.assertRaises(DuplicateCardError, get_remaining_cards, players, board_with_duplicate)


if __name__ == '__main__':
    unittest.main()
