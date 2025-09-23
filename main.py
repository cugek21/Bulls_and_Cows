"""Bulls and Cows Game - Main Module

A number guessing game also known as Mastermind with numbers.
Players try to guess a randomly generated number, receiving feedback
in the form of 'bulls' (correct digit, correct position) and
'cows' (correct digit, wrong position).

Features:
- Random number generation
- Input validation
- Time tracking
- High score system
- Multiple round support
- Python version checking

Author: Radek Jíša
Email: radek.jisa@gmail.com
"""

import random
import time
import sys

from game_functions import (
    introduction, get_user_input, evaluate_guess, get_plurals,
    calculate_time, highscore, end_credits, ask_to_continue,
    CENTER_WIDTH, NUMBER_LENGTH, MIN_NUMBER, MAX_NUMBER, DIVIDER
)


def check_python_version(required=(3, 10)):
    """
    Raises an error if the Python version is below the required.
    
    Args:
        required (tuple): Required Python version as (major, minor).

    Raises:
        RuntimeError: If current version is lower than required.
    """
    current = sys.version_info
    if current[:2] < required:
        raise RuntimeError(
        f'Requires Python {required[0]}.{required[1]}+, '
        f'but found {current.major}.{current.minor}'
        )


def play_game() -> None:
    """Main game loop for Bulls and Cows.
    
    Manages the game flow including:
    - Displaying introduction and game interface
    - Generating random numbers
    - Processing user input
    - Tracking attempts and time
    - Managing multiple game rounds
    """
    first_game = True
    while True:
        if first_game:
            print(introduction(DIVIDER))
            first_game = False
        else:
            print(f'\n{DIVIDER}')
        generated_number = list(str(random.randint(MIN_NUMBER, MAX_NUMBER)))
        attempts = 0
        start_time = None

        while True:
            print(f'\n{'Enter the number:'.center(CENTER_WIDTH)}')
            user_number = get_user_input()
            if start_time is None:
                start_time = time.time()

            bulls, cows = evaluate_guess(generated_number, user_number)
            bulls_word, cows_word = get_plurals(bulls, cows)

            print(f'{bulls_word.capitalize()} {bulls:^34} {cows:^35} {cows_word.capitalize()}')
            attempts += 1            
            if bulls == NUMBER_LENGTH:
                end_time = time.time()
                break

        mins, secs, score = calculate_time(start_time, end_time)
        high_scores = highscore(score)
        print(end_credits(DIVIDER, mins, secs, high_scores, attempts))
        if not ask_to_continue():
            break


if __name__ == "__main__":
    check_python_version((3,10))
    play_game()
