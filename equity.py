from random import randint, shuffle
from hands import *
from copy import deepcopy
from settings import *


def create_deck():
    # create the full deck:
    deck = [{'suit': suits[suit], 'val': cardvals[card]} for suit in range(numsuits) for card in range(cardspersuit)]
    return deck


deck = create_deck()



def getval(card):
    return card['val'] # function to enable the cards to be sorted by value



def get_vals(cards):
    return sorted([card['val'] for card in cards], reverse=True)

def kickers_calculator(cards_vals, kickers_needed, *cards_used):
    possible_kickers = [card for card in cards_vals if card not in cards_used]
    if possible_kickers:
        kickers = [possible_kickers.pop(0) for _ in range(kickers_needed)]
        return kickers
    else:
        return []

def checkstraight(cards_vals_unique):
    for i in range(len(cards_vals_unique) - 4):
        if cards_vals_unique[i] - cards_vals_unique[i + 4] == 4:
            return cards_vals_unique[i]
    return None

placeholder_hand = [{'suit': 'Z', 'val': 0}, {'suit': 'Z', 'val': 0}, {'suit': 'Z', 'val': 0}, {'suit': 'Z', 'val': 0}, {'suit': 'Z', 'val': 0}, {'suit': 'Z', 'val': 0}, {'suit': 'Z', 'val': 0}]

def highcard(cards = placeholder_hand):
    cards = sorted(cards, key=lambda card: card['val'], reverse=True)
    return cards[0]['val']
# print(f'highcard: {highcard(cards)}')

def pair(cards = placeholder_hand, kickers_needed = True):
    cards = sorted(cards, key=lambda card: card['val'], reverse=True)
    cards_vals = get_vals(cards)
    numcards = len(cards)
    for c in range(numcards-1):
        if cards_vals[c] == cards_vals[c + 1]:
            if kickers_needed:
                return [cards_vals[c], cards_vals[c], *kickers_calculator(cards_vals, 3, cards_vals[c])]
            else:
                return [cards_vals[c], cards_vals[c]]
    return None
# print(f'pair: {pair(cards)}')

def twopair(cards = placeholder_hand, kickers_needed = True):
    cards = sorted(cards, key=lambda card: card['val'], reverse=True)
    cards_vals = get_vals(cards)
    # if there is no pair there cannot be a twopair
    pairchecker = pair(cards, False)
    if pairchecker is not None:
        top = pairchecker[0]
    else:
        return None
    cards = [card for card in cards if card['val'] != top]
    pairchecker = pair(cards, False)
    if pairchecker is not None:
        bottom = pairchecker[0]
    else:
        return None
    kickers = kickers_calculator(cards_vals, 1, top, bottom)
    if kickers_needed:
        return [top, top, bottom, bottom, *kickers]
    else:
        return [top, top, bottom, bottom]
# print(f'two: {twopair(cards)}')
                
def trips(cards = placeholder_hand, kickers_needed = True):
    cards = sorted(cards, key=lambda card: card['val'], reverse=True)
    cards_vals = get_vals(cards)
    numcards = len(cards)
    for c in range(numcards-2):
        if cards_vals[c] == cards_vals[c + 1] == cards_vals[c+2]:
            if kickers_needed:
                return [cards_vals[c], cards_vals[c], cards_vals[c], *kickers_calculator(cards_vals, 2, cards_vals[c])]
            else:
                return [cards_vals[c], cards_vals[c], cards_vals[c]]
    return None
# print(f'trips: {trips(cards)}')

def straight(cards = placeholder_hand):
    cards = sorted(cards, key=lambda card: card['val'], reverse=True)
    cards_vals = get_vals(cards)
    cards_vals_unique = sorted(set(cards_vals), reverse = True)
    if checkstraight(cards_vals_unique) is not None:
        return checkstraight(cards_vals_unique)
    
    # Check again where Ace can make bottom of straight
    cards_vals_unique = sorted([1 if card == 14 else card for card in cards_vals_unique], reverse = True)
    if checkstraight(cards_vals_unique) is not None:
        return checkstraight(cards_vals_unique)
    
    return None
# print(f"straight: {straight(cards)}")

def flush(cards = placeholder_hand, return_all_suited = False):
    cards = sorted(cards, key=lambda card: card['val'], reverse=True)
    # Count occurence of each suit and store in dictionary
    suit_count = {'S': 0, 'H': 0, 'D': 0, 'C': 0}
    for card in cards:
        suit = card['suit']
        if suit in suit_count:
            suit_count[suit] += 1
    # If flush is found return top 5 cards of that suit otherwise return None
    for suit, count in suit_count.items():
        if count >= 5:
            winning_suit = suit
            suited = get_vals([card for card in cards if card['suit'] == winning_suit])
            if return_all_suited is False:
                return suited[:5]
            else:
                return suited
    return None
# print(f"flush: {flush(cards)}")

def full_house(cards = placeholder_hand):
    cards = sorted(cards, key=lambda card: card['val'], reverse=True)
    tripchecker = trips(cards, kickers_needed = False)
    if tripchecker is None:
        return None
    else:
        three_same_cards = tripchecker[0]
    cards = [card for card in cards if card['val'] != three_same_cards]
    pairchecker = pair(cards, kickers_needed = False)
    if pairchecker is None:
        return None
    return [*tripchecker, *pairchecker]
# print(f"full house: {full_house(cards)}")
            
def quads(cards = placeholder_hand, kickers_needed = True):
    cards = sorted(cards, key=lambda card: card['val'], reverse=True)
    cards_vals = get_vals(cards)
    numcards = len(cards)
    for c in range(numcards-3):
        if cards_vals[c] == cards_vals[c + 1] == cards_vals[c+2] == cards_vals[c+3]:
            if kickers_needed:
                return [*[cards_vals[c] for _ in range(4)], *kickers_calculator(cards_vals, 1, cards_vals[c])]
            else:
                return [cards_vals[c] for _ in range(4)]
    return None
# print(f"quads: {quads(cards)}")
    
def straight_flush(cards = placeholder_hand):
    cards = sorted(cards, key=lambda card: card['val'], reverse=True)
    suited = flush(cards, return_all_suited = True)
    if suited is None:
        return None
    if checkstraight(suited) is not None:
        return checkstraight(suited)
    
    # Check again where Ace can make bottom of straight
    suited = sorted([1 if card == 14 else card for card in suited], reverse = True)
    if checkstraight(suited) is not None:
        return checkstraight(suited)
    return None
# print(f"straight flush: {straight_flush(cards)}")

def royal_flush(cards = placeholder_hand):
    cards = sorted(cards, key=lambda card: card['val'], reverse=True)
    check_straight_flush = straight_flush(cards)
    if check_straight_flush is None:
        return None
    elif check_straight_flush != 14:
        return None
    else:
        return 14
# print(f"royal flush: {royal_flush(cards)}")

hands_ranking_strings = ["royal_flush", "straight_flush", "quads", "full_house", "flush", "straight", "trips", "twopair", "pair", "highcard"]

hands_ranking = [royal_flush, straight_flush, quads, full_house, flush, straight, trips, twopair, pair, highcard]



def get_hand_ranking(cards):
    for hand in hands_ranking:
        if hand(cards) is not None:
            return hands_ranking.index(hand)

# players = [{"name": "Seb", "hand": Ace_King_Hearts}, {"name": "Dom", "hand": Black_Queens}]

def get_winners(players, return_idx = False, return_names = True):
    hands = [person["hand"] for person in players]
    lowest_score = 100
    winners_hand = None
    for hand in hands:
        score = get_hand_ranking(hand)
        # Check if hand ranking is worse, if so continue
        if score > lowest_score:
            continue
        # Check if hand ranking is better, if so add to winners_hand
        elif score < lowest_score:
            lowest_score = score
            winners_hand = [hand]

        else:
            # Gets the hand type to compare, e.g. quads
            hand_type = hands_ranking[lowest_score]
            new_hand_in_play = hand_type(hand)
            old_hand_in_play = hand_type(winners_hand[0])
            # Checks if hands are identical, if so adds another winner meaning chop
            if new_hand_in_play == old_hand_in_play:
                winners_hand.append(hand)
            else:
                for _ in range(len(hand) - 1):
                    if new_hand_in_play > old_hand_in_play:
                        winners_hand = [hand]
                    if new_hand_in_play < old_hand_in_play:
                        break

    if return_idx:
        return lowest_score

    if return_names:
        winner_names = [person["name"] for person in players if person["hand"] in winners_hand]
        return winner_names

    return winners_hand





def create_winners(players):
    hands = [person["hand"] for person in players]
    winners = []
    for hand in get_winners(hands):
        for person in players:
            if (hand == person["hand"]) and (person["name"] not in winners):
                winners.append(person["name"])
    return winners

def print_result(players, winners):
    hands = [person["hand"] for person in players]
    if len(winners) > 1:
        print("Chop between ", end="")
        for i, name in enumerate(winners):
            if i > 0:
                print(" and ", end="")
            print(name, end="")
            print(f" with {hands_ranking_strings[get_winners(hands, return_idx = True)]} containing {get_winners(hands)[0]}", end = "")

    else:
        print(f"{winners[0]} wins the hand with {hands_ranking_strings[get_winners(hands, return_idx = True)]} containing {get_winners(hands)[0]}")
    return 0

class DuplicateCardError(Exception):
    pass

def get_remaining_cards(players, board, return_used=False):
    full_deck = create_deck()
    
    # Flatten all hands into a single list
    cards_in_hands = [card for person in players for card in person["hand"]]
    all_cards = cards_in_hands + board
    
    # Check for duplicates
    seen_cards = set()
    for card in all_cards:
        card_tuple = (card['val'], card['suit'])  # Use a tuple for easier comparison
        if card_tuple in seen_cards:
            raise DuplicateCardError
        seen_cards.add(card_tuple)

    if return_used:
        used_cards = [card for card in full_deck if (card['val'], card['suit']) in seen_cards]
        return used_cards
    
    # Filter out cards in hands from the full deck
    remaining_deck = [card for card in full_deck if (card['val'], card['suit']) not in seen_cards]
    return remaining_deck


    



def create_final_hands(players, final_board):
    final_hands = deepcopy(players)
    for player in final_hands:
        for card in final_board:
            player["hand"].append(card)
    return final_hands
    
        


def calculate_equity(players, board, numiterations):
    # Work out how many more cards are needed to add to the board
    boardlen = len(board)
    neededcards = 0
    if boardlen < 5:
        neededcards = 5 - boardlen
    # Check if initial board is valid
    acceptedable_needed = [0, 1, 2, 5]
    if neededcards not in acceptedable_needed:
        print("invalid board")
        exit()

    remaining_deck = get_remaining_cards(players, board)
    winners_list = []
    original_remaining_deck = deepcopy(remaining_deck)
    for _ in range(numiterations):
        remaining_deck = deepcopy(original_remaining_deck)
        shuffle(remaining_deck)
        
        final_board = deepcopy(board)
        for _ in range(neededcards):
            final_board.append(remaining_deck.pop(0))
        final_hands = create_final_hands(players, final_board)
        winner = get_winners(final_hands)
        winners_list.append(winner)
    results_list = []
    # print(winners_list)
    for winner in winners_list:
        if len(winner) == 1:
            results_list.append(winner[0])
        else:
            results_list.append(None)
    return results_list

def display_results(players, board, results_list):
    card_value_map_to_str = {
        "2": "Two", "Two": "Two", 
        "3": "Three", "Three": "Three", 
        "4": "Four", "Four": "Four", 
        "5": "Five", "Five": "Five", 
        "6": "Six", "Six": "Six", 
        "7": "Seven", "Seven": "Seven", 
        "8": "Eight", "Eight": "Eight", 
        "9": "Nine", "Nine": "Nine", 
        "10": "Ten", "Ten": "Ten", 
        "11": "Jack", "J": "Jack", "Jack": "Jack", 
        "12": "Queen", "Q": "Queen", "Queen": "Queen", 
        "13": "King", "K": "King", "King": "King", 
        "14": "Ace", "A": "Ace", "Ace": "Ace", "1": "Ace"
    }

    suits_map_to_str = {
        "S": "Spades", "Spades": "Spades", "Spade": "Spades", 
        "H": "Hearts", "Hearts": "Hearts", "Heart": "Hearts", 
        "D": "Diamonds", "Diamonds": "Diamonds", "Diamond": "Diamonds", 
        "C": "Clubs", "Clubs": "Clubs", "Club": "Clubs"
    }

    names = [player["name"] for player in players]
    equities = []
    for name in names:
        count = results_list.count(name)
        equity = count / numiterations
        equities.append({"name": name, "equity": f"{round(equity * 100, 2)}%"})
    
    chop_equity = results_list.count(None) / numiterations
    chop_equity = f"{round(chop_equity * 100, 2)}%"
    if len(board) != 0:
        print("The board contains the ", end = "")
        for idx in range(len(board)):
            card_value = board[idx]['val']
            card_suit = board[idx]['suit']
            
            print(f"{card_value_map_to_str[str(card_value)]} of {suits_map_to_str[card_suit]}", end = "")
            if idx == len(board) - 2:
                print(", and the ", end = "")
            elif idx == len(board) - 1:
                print(".")
            else:
                print(", ", end = "")
    else:
        print("On an empty board: ")

    for idx in range(len(players)):
        print(f"{players[idx]['name']} has {equities[idx]['equity']} equity with the ", end="")
        

        for card in range(hole_cards_per_hand):
            card_value = players[idx]['hand'][card]['val']
            card_suit = players[idx]['hand'][card]['suit']
            
            print(f"{card_value_map_to_str[str(card_value)]} of {suits_map_to_str[card_suit]}", end = "")
            
            if card == hole_cards_per_hand - 2:
                print(", and the ", end = "")
            elif card == hole_cards_per_hand - 1:
                print(".")
            else:
                print(", ", end = "")


    print(f"The chance of a chop is {chop_equity}.")
    return 0


def check_input_for_stop(input):
    """Returns True if player wants to stop inputs"""
    if input.strip().lower() == "stop" or input.strip().lower() == "":
        return True

def take_input():
    card_value_map = {
    "2": 2, "Two": 2, "3": 3, "Three": 3, "4": 4, "Four": 4, "5": 5, "Five": 5, "6": 6, "Six": 6, "7": 7, "Seven": 7, "8": 8, "Eight": 8, "9": 9, "Nine": 9, "10": 10, "Ten": 10,
    "11": 11, "J": 11, "Jack": 11,
    "12": 12, "Q": 12, "Queen": 12,
    "13": 13, "K": 13, "King": 13,
    "14": 14, "A": 14, "Ace": 14, "1": 14,
}

    suits_map = {
    "S": "S", "Spades": "S", "Spade": "S", 
    "H": "H", "Hearts": "H", "Heart": "H",
    "D": "D", "Diamonds": "D", "Diamond": "D",
    "C": "C", "Clubs": "C", "Club": "C"
    }
    

    checking_player_inputs = True
    players = []
    board = []
    cards_per_hand = 2
    while checking_player_inputs:
        cards_in_hand = 0
        print("Type stop or press enter when you have finished!")
        input_name = str(input("Please enter player name: "))
        if check_input_for_stop(input_name):
            break
        for player in players:
            if player["name"] == input_name:
                print("Name already in use!")
                continue
        players.append({"name": input_name, "hand": []})
        while cards_in_hand < cards_per_hand:
            input_val = input("Please enter a card value: ")
            if check_input_for_stop(input_val):
                players = [player for player in players if player.get("name") != input_name]
                checking_player_inputs = False
                break
            input_val = str(input_val).strip().capitalize()
            
            # Get the corresponding card value from the dictionary
            if input_val in card_value_map:
                input_val = card_value_map[input_val]
            else:
                print("Incorrect card value inputted!")
                continue
            input_suit = input("Please enter the suit of the card: ")
            if check_input_for_stop(input_suit):
                players = [player for player in players if player.get("name") != input_name]
                checking_player_inputs = False
                break
            input_suit = str(input_suit).strip().capitalize()
            if input_suit in suits_map:
                input_suit = suits_map[input_suit]
            else:
                print("Incorrect card suit inputted!")
                continue
            # Add card to correct player
            card = {"val": input_val, "suit": input_suit}
            if card not in get_remaining_cards(players, board, True):
                player = next((p for p in players if p["name"] == input_name), None)
                if player:
                    player["hand"].append({"val": input_val, "suit": input_suit})
                    cards_in_hand += 1
                else:
                    print(f"Player {input_name} not found!")
                    continue
            else:
                print("Card already in use!")
                continue


    
    print("Now add cards to the board, press enter or type stop when finished")
    checking_board_inputs = True
    while checking_board_inputs:
        input_val = input("Please enter a card value: ")
        if check_input_for_stop(input_val):
            checking_board_inputs = False
            break
        input_val = str(input_val).strip().capitalize()
        if input_val in card_value_map:
            input_val = card_value_map[input_val]
        else:
            print("Incorrect card value inputted!")
            continue
        input_suit = input("Please enter the suit of the card: ")

        if check_input_for_stop(input_suit):
                checking_board_inputs = False
                break
        input_suit = str(input_suit).strip().capitalize()
        if input_suit in suits_map:
            input_suit = suits_map[input_suit]
        else:
            print("Incorrect card suit inputted!")
            continue
        card = {"val": input_val, "suit": input_suit}
        if card not in get_remaining_cards(players, board, True):
            board.append(card)
        else:
            print("Card already in use!")
            continue
    return players, board


def test_players_board():
    name1 = "You"
    name2 = "Others"
    hand1 = [{"val": 14, "suit": "H"}, {"val": 11, "suit": "S"}]
    hand2 = [{"val": 4, "suit": "S"}, {"val": 4, "suit": "C"}]
    board = [{"val": 13, "suit": "C"}, {"val": 10, "suit": "C"}, {"val": 14, "suit": "C"}]
    players = [{"name": name1, "hand": hand1}, {"name": name2, "hand": hand2}]
    return players, board


testing = False
def main():
    if testing:
        players, board = test_players_board()
    else:
        players, board = take_input()
    results_list = calculate_equity(players, board, numiterations)
    display_results(players, board, results_list)

if __name__ == "__main__":
    main()