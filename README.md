# Poker Equity Calculator

A Monte Carlo simulation-based equity calculator for Texas Hold'em and Omaha poker.

## What it does

Calculates the winning probability (equity) for each player given their hole cards and the board cards. Supports both:

- **Texas Hold'em**: 2 hole cards per player
- **Omaha**: 4 hole cards per player

## How to run

```bash
python equity.py
```

## Usage

The program will prompt you for:

1. Game type (Texas Hold'em or Omaha)
2. Number of players
3. Each player's hole cards (e.g., `A s K h` for Ace of spades, King of hearts)
4. Board cards

Card format: `rank + suit` where:

- Ranks: `A`, `K`, `Q`, `J`, `T`, `9`-`2`
- Suits: `s` (spades), `h` (hearts), `d` (diamonds), `c` (clubs)
