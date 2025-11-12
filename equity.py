from random import shuffle
import itertools
# Try to get vals for cards then use them for the functions which only need vals

def create_deck():
    # create the full deck:
    deck = list(range(1, 53))
    return deck

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]


def get_vals(cards):
    return sorted([(card - 1) % 13 + 1 for card in cards], reverse = True)
def get_val(card):
    return ((card - 1) % 13) + 1
def get_suit(card):
    return suits[(card - 1) // 13]
    

def kickers_calculator(vals, kickers_needed, *cards_used):
    possible_kickers = [card for card in vals if card not in cards_used]
    if possible_kickers:
        kickers = [possible_kickers.pop(0) for _ in range(kickers_needed)]
        return kickers
    else:
        return []

def checkstraight(unique_vals_desc):
    for i in range(len(unique_vals_desc) - 4):
        if unique_vals_desc[i] - unique_vals_desc[i + 4] == 4:
            return unique_vals_desc[i]
    return None

def highcard(vals):
    vals = get_vals(vals)
    return vals[0]
def pair(vals, kickers_needed = True):
    vals = get_vals(vals)
    numcards = len(vals)
    for c in range(numcards-1):
        val = vals[c]
        if val == vals[c + 1]:
            if kickers_needed:
                return [val, val, *kickers_calculator(vals, 3, val)]
            else:
                return [val, val]
    return None

def twopair(cards, kickers_needed = True):
    # if there is no pair there cannot be a twopair
    vals = get_vals(cards)
    pairchecker = pair(vals, False)
    
    if pairchecker is None:
        return None
    else:
        top = pairchecker[0]
    
    vals = [val for val in vals if val != top]
    pairchecker = pair(vals, False)

    if pairchecker is None:
        return None
    else:
        bottom = pairchecker[0]

    kickers = kickers_calculator(vals, 1, top, bottom)
    if kickers_needed:
        return [top, top, bottom, bottom, *kickers]
    else:
        return [top, top, bottom, bottom]
                
def trips(vals, kickers_needed = True):
    vals = get_vals(vals)
    numcards = len(vals)
    for c in range(numcards-2):
        val = vals[c]
        if val == vals[c + 1] == vals[c+2]:
            if kickers_needed:
                return [val, val, val, *kickers_calculator(vals, 2, val)]
            else:
                return [val, val, val]
    return None

def straight(vals):
    vals = get_vals(vals)
    unique_vals_desc = sorted(set(vals), reverse = True)
    result = checkstraight(unique_vals_desc)
    if result is not None:
        return result
    
    # Check again where Ace can make bottom of straight
    if {2, 3, 4, 5, 14}.issubset(vals):
        return 5
    
    return None

def flush(cards, return_all_suited = False):
    cards = sorted(cards, reverse = True)
    # Count occurence of each suit and store in dictionary
    suit_count = [((card-1) // 13) for card in cards]
    # If flush is found return top 5 cards of that suit otherwise return None
    for suit in range(4):
        if suit_count.count(suit) > 4:
            suited = [card for card in cards if ((card-1) // 13) == suit]
            break
    else:
        return None
    return suited if return_all_suited else suited[:5]
    
def full_house(vals):
    vals = get_vals(vals)
    tripchecker = trips(vals, kickers_needed = False)
    if tripchecker is None:
        return None
    else:
        three_same_cards = tripchecker[0]
    vals = [val for val in vals if val != three_same_cards]
    pairchecker = pair(vals, kickers_needed = False)
    if pairchecker is None:
        return None
    return [*tripchecker, *pairchecker]
            
def quads(vals, kickers_needed = True):
    vals = get_vals(vals)
    numcards = len(vals)
    for c in range(numcards-3):
        val = vals[c]
        if val == vals[c + 1] == vals[c+2] == vals[c+3]:
            if kickers_needed:
                return [*[val for _ in range(4)], *kickers_calculator(vals, 1, val)]
            else:
                return [val for _ in range(4)]
    return None

wheel_straight_flushes = [{1, 2, 3, 4, 13}, {14, 15, 16, 17, 25}, {27, 28, 29, 30, 39}, {40, 41, 42, 43, 52}]

def straight_flush(cards):
    # First check if there's a flush
    suited_cards = flush(cards, return_all_suited = True)
    if suited_cards is None:
        return None

    # Then check if the suited cards form a straight
    result = checkstraight(suited_cards)
    if result is not None:
        return result

    # Check for wheel straight flush (A-2-3-4-5)
    for wheel in wheel_straight_flushes:
        if wheel.issubset(cards):
            return 5
    return None

def royal_flush(cards):
    result = straight_flush(cards)
    return 13 if result == 13 else None

hands_ranking_strings = ["royal_flush", "straight_flush", "quads", "full_house", "flush", "straight", "trips", "twopair", "pair", "highcard"]

hands_ranking = [royal_flush, straight_flush, quads, full_house, flush, straight, trips, twopair, pair, highcard]



def get_hand_ranking(cards):
    for idx, hand in enumerate(hands_ranking):
        if hand(cards) is not None:
            return idx



def get_winners(players, return_idx=False, return_names=True, num_hole_cards=2):
    hands = [person["hand"] for person in players]
    lowest_score = float('inf')
    winners_hand = []   
    for hand in hands:
        score = get_hand_ranking(hand)
        # Check if hand ranking is worse, if so continue, lower score is better
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
            elif new_hand_in_play > old_hand_in_play:
                winners_hand = [hand]
    
    if return_idx:
        return lowest_score

    if return_names:
        winner_names = []
        if num_hole_cards == 2:
            winner_names = [person["name"] for person in players if person["hand"] in winners_hand]
        elif num_hole_cards == 4:
            for player in players:
                if (player["hand"] in winners_hand and player["name"] not in winner_names):
                    winner_names.append(player["name"])
        return winner_names

    return winners_hand

class DuplicateCardError(Exception):
    pass

def get_remaining_cards(players, board, return_used=False):
    # Flatten all hands into a single list
    cards_in_hands = [card for person in players for card in person["hand"]]
    all_cards = cards_in_hands + board
    # Check for duplicates
    if len(set(all_cards)) != len(all_cards):
        raise DuplicateCardError

    used_cards_set = set(all_cards)
    full_deck = list(range(1, 53))

    if return_used:
        return [card for card in full_deck if card in used_cards_set]
    return [card for card in full_deck if card not in used_cards_set]



def create_final_hands_texas(players, final_board):
    final_hands = []
    for player in players:
        final_hands.append({"name": player["name"], "hand": player["hand"] + final_board})
    return final_hands


def create_final_hands_omaha(players, board):

    final_hands = []

    # For each player
    for player in players:
        player_name = player["name"]
        player_hand = player["hand"]

        # Get all combinations of 2 cards from the player's 4-card hand
        player_combinations = list(itertools.combinations(player_hand, 2))
        board_combinations = list(itertools.combinations(board, 3))

        for hole_cards in player_combinations:
            for board_combination in board_combinations:
                final_hands.append({"name": player_name, "hand": list(hole_cards) + list(board_combination)})

        
    
    return final_hands


def calculate_equity_mc(players, board, numiterations, num_hole_cards):
    boardlen = len(board)
    neededcards = 0
    if boardlen < 5:
        neededcards = 5 - boardlen
    
    acceptable_needed = [0, 1, 2, 5]
    if neededcards not in acceptable_needed:
        print("invalid board")
        exit()
    
    # Get remaining deck once for baseline state
    original_remaining_deck = get_remaining_cards(players, board)  # list of ints
    winners_list = []
    
    for _ in range(numiterations):
        # Copy deck by slicing, then shuffle in place
        remaining_deck = original_remaining_deck[:]
        shuffle(remaining_deck)
        
        # Copy board by slicing, then add needed cards
        final_board = board[:]
        for _ in range(neededcards):
            final_board.append(remaining_deck.pop(0))
        
        if num_hole_cards == 2:
            final_hands = create_final_hands_texas(players, final_board)
        else:
            final_hands = create_final_hands_omaha(players, final_board)
        
        winner = get_winners(final_hands, num_hole_cards=num_hole_cards)
        winners_list.append(winner)
    
    results_list = []
    for winner in winners_list:
        if len(winner) == 1:
            results_list.append(winner[0])
        else:
            results_list.append(None)
    return results_list

def display_results(players, board, results_list, numiterations, num_hole_cards):
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
            card_value = get_val(board[idx])
            card_suit = get_suit(board[idx])
            print(f"{card_value_map_to_str[str(card_value + 1)]} of {suits_map_to_str[card_suit]}", end = "")
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
        

        for card in range(num_hole_cards):
            card_value = get_val(players[idx]['hand'][card])
            card_suit = get_suit(players[idx]['hand'][card])
            
            print(f"{card_value_map_to_str[str(card_value + 1)]} of {suits_map_to_str[card_suit]}", end = "")
            
            if card == num_hole_cards - 2:
                print(", and the ", end = "")
            elif card == num_hole_cards - 1:
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
    "S": 0, "Spades": 0, "Spade": 0, 
    "H": 1, "Hearts": 1, "Heart": 1,
    "D": 2, "Diamonds": 2, "Diamond": 2,
    "C": 3, "Clubs": 3, "Club": 3
    }


    checking_player_inputs = True
    players = []
    board = []

    checking_game = True
    while checking_game:
        game = str(input((f"Welcome to the poker equity calculator, type \"Texas\" or hit Enter for Texas Hold'em or \"Omaha\" for Omaha:\n")))
        if game.strip().lower() == "texas" or game == "":
            num_hole_cards = 2
            numiterations = 40000
            print("Texas Hold'em selected")
            break
        elif game.strip().lower() == "omaha":
            num_hole_cards = 4
            numiterations = 5000
            print("Omaha selected")
            break
        else:
            print("Incorrect game mode! Please try again.")
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
        while cards_in_hand < num_hole_cards:
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
            card = 13 * input_suit + (input_val - 1)
            if card not in get_remaining_cards(players, board, True):
                player = next((p for p in players if p["name"] == input_name), None)
                if player:
                    player["hand"].append(card)
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
        card = 13 * input_suit + (input_val - 1)
        if card not in get_remaining_cards(players, board, True):
            board.append(card)
        else:
            print("Card already in use!")
            continue
    return players, board, num_hole_cards, numiterations

def main():
    players, board, hole_cards, iterations = take_input()
    results_list = calculate_equity_mc(players, board, iterations, hole_cards)
    display_results(players, board, results_list, iterations, hole_cards)

if __name__ == "__main__":
    main()