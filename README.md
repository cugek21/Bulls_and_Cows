# Bulls and Cows Game

A command-line implementation of the classic Bulls and Cows game (also known as Mastermind with numbers). Players attempt to guess a randomly generated number while receiving feedback in the form of 'bulls' (correct digit, correct position) and 'cows' (correct digit, wrong position).

## Features

- 🎯 4-digit number guessing game
- ✅ Input validation
- ⏱️ Time tracking
- 🏆 Top 10 high scores system
- 🔄 Multiple round support
- 📊 Game statistics (attempts, time)
- 🎮 User-friendly interface

## Requirements

- Python 3.10 or higher
- No additional packages required

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. The game will generate a random 4-digit number for you to guess.

3. Enter your guess when prompted:
   - Must be a 4-digit number
   - Cannot start with zero
   - Each guess will show you the number of bulls and cows

4. Keep guessing until you get the correct number (4 bulls).

5. After winning:
   - See your completion time
   - View your number of attempts
   - Check the high scores
   - Choose to play again or quit

## Game Rules

- **Bulls**: Correct digits in correct positions
- **Cows**: Correct digits in wrong positions
- Each digit in the target number can only be matched once
- The game tracks the time taken to guess the number correctly

## Project Structure

```
Cows_and_Bulls/
├── main.py              # Game entry point and main loop
├── game_functions.py    # Core game functionality
├── highscore.txt       # High scores storage
└── README.md           # Project documentation
```

## High Score System

- Maintains a list of top 10 fastest completion times
- Scores are stored in `highscore.txt`
- Lower completion times are better
- Persists between game sessions

## Author

Radek Jíša  
radek.jisa@gmail.com