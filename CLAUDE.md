# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A poker equity calculator that computes win probabilities for Texas Hold'em and Omaha poker hands using Monte Carlo simulation. The calculator evaluates hand rankings (royal flush through high card) and simulates remaining community cards to determine each player's winning probability.

## Running the Application

```bash
python equity.py
```

The program will prompt for:

1. Game type (Texas Hold'em or Omaha)
2. Player names and hole cards (2 cards for Texas, 4 for Omaha)
3. Board cards (up to 5 community cards)

## Code Architecture

### Card Representation

Cards are represented as integers 1-52:

- Card value: `(card - 1) % 13 + 1` (1=Ace low, 13=King, 14=Ace high in some contexts)
- Card suit: `(card - 1) // 13` (0=Spades, 1=Hearts, 2=Diamonds, 3=Clubs)
- Example: Card 1 = Ace of Spades, Card 52 = King of Clubs

### Core Components

**[equity.py](equity.py)** - Single file containing all logic:

- Hand evaluation functions (`royal_flush`, `straight_flush`, `quads`, `full_house`, `flush`, `straight`, `trips`, `twopair`, `pair`, `highcard`)
- Monte Carlo equity calculator (`calculate_equity_mc`)
- Game logic for both Texas Hold'em and Omaha
- User input handling and results display

### Hand Evaluation System

The `hands_ranking` list in [equity.py](equity.py) defines hand strength from strongest to weakest. Each function returns either:

- `None` if the hand type is not present
- An integer or list of values representing the hand strength for comparison

Hand comparison uses the returned values directly - higher values indicate stronger hands (except for hand ranking index where lower is better).

### Game Type Differences

**Texas Hold'em** ([equity.py:241](equity.py#L241)):

- Uses 2 hole cards per player
- Final hand = all 7 cards (2 hole + 5 board)
- Function: `create_final_hands_texas(players, final_board)`

**Omaha** ([equity.py:248](equity.py#L248)):

- Uses 4 hole cards per player
- Must use exactly 2 hole cards and 3 board cards
- Function: `create_final_hands_omaha(players, board)` generates all valid combinations (C(4,2) × C(5,3) = 60 combinations per player)

### Monte Carlo Simulation

The equity calculator ([equity.py:269](equity.py#L269)) works by:

1. Accepting parameters: `players`, `board`, `numiterations`, `num_hole_cards`
2. Removing known cards (player hands + board) from the deck
3. For each iteration:
   - Shuffling remaining cards
   - Dealing out missing board cards (if flop/turn/preflop)
   - Creating final hands based on game type
   - Determining winner(s)
4. Calculating each player's win percentage from simulation results

**Parameter Passing**: All configuration (number of hole cards, iterations) is passed as function parameters, not globals. This allows proper handling of different game types without state management issues.

### User Input Flow

The `take_input()` function ([equity.py:386](equity.py#L386)):

1. Prompts for game type (Texas or Omaha)
2. Sets appropriate values for `num_hole_cards` and `numiterations`
3. Collects player names and hole cards
4. Collects board cards
5. Returns `(players, board, num_hole_cards, numiterations)` as a tuple

## Key Functions to Know

- `get_remaining_cards(players, board, return_used=False)` - Returns available cards from deck (or used cards if `return_used=True`)
- `get_winners(players, return_idx=False, return_names=True, num_hole_cards=2)` - Determines winning hand(s) from a set of complete hands
- `create_final_hands_texas(players, final_board)` - Creates 7-card hands for Texas Hold'em
- `create_final_hands_omaha(players, board)` - Creates all valid 5-card combinations for Omaha
- `calculate_equity_mc(players, board, numiterations, num_hole_cards)` - Main Monte Carlo simulation engine
- `display_results(players, board, results_list, numiterations, num_hole_cards)` - Formats and displays equity percentages

## Important Implementation Details

### Bug Fixes Applied

1. **Straight Flush Bug Fixed**: The `straight_flush()` function now correctly checks that cards are suited before checking for straights. Previously would incorrectly identify mixed-suit straights as straight flushes.

2. **Settings Refactor**: Removed global variable usage. All configuration is passed as function parameters to avoid state management issues when switching between game types.

3. **Winner Determination**: The `get_winners()` function now properly handles both Texas Hold'em and Omaha by accepting `num_hole_cards` as a parameter. This fixes an issue where Omaha games would fail due to uninitialized variables.

### Code Cleanup Applied

- Removed unused imports (`randint`, `deepcopy`)
- Removed dead code (test functions that were never called)
- Removed duplicate functions (`card_to_num()`)
- Simplified hand evaluation logic (`royal_flush()`, `flush()`)
- Removed unnecessary module-level constants (`FULL_DECK`)

## Testing Notes

When adding new hand evaluation logic, add corresponding test cases in the tests/ directory following the existing unittest pattern. Tests currently use a dictionary-based card format and may need refactoring to use the integer representation.
