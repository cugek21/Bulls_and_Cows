"""Bulls and Cows Game - Functions Module

This module contains all the core functionality for the Bulls and Cows game.
It provides functions for game logic, user interaction, and score management.

Core Components:
- Game mechanics (bulls and cows counting)
- User input handling and validation
- Time tracking and score management
- Display formatting and text generation
- High score file management

Constants:
    CENTER_WIDTH (int): Width for text centering
    NUMBER_LENGTH (int): Length of the number to guess
    MIN_NUMBER (int): Minimum possible number
    MAX_NUMBER (int): Maximum possible number
    DIVIDER (str): Visual separator for display
    HIGHSCORE_FILE (Path): Path to the high score file

Author: Radek Jíša
Email: radek.jisa@gmail.com
"""

from pathlib import Path

HIGHSCORE_FILE = Path('highscore.txt')

CENTER_WIDTH = 80
NUMBER_LENGTH = 4
MIN_NUMBER = 1000
MAX_NUMBER = 9999
DIVIDER = '-' * CENTER_WIDTH


def introduction(divider: str) -> str:
    """Generate the game's introduction message.
    
    Creates a formatted welcome screen with game title and instructions.
    
    Args:
        divider (str): String used to create visual separators
        
    Returns:
        str: Formatted introduction message with centered text and dividers
    """
    return f'''
{divider}\n
{'BULLS and COWS'.center(CENTER_WIDTH)}\n
{'aka'.center(CENTER_WIDTH)}
{'\'Mastermind\''.center(CENTER_WIDTH)}\n
{divider}\n
{f'I\'ve generated a random {NUMBER_LENGTH} digit number for you.'.center(CENTER_WIDTH)}
{'Guess which one is it.'.center(CENTER_WIDTH)}\n
{divider}'''


def get_user_input() -> list[str]:
    """Get and validate user's number guess.
    
    Prompts the user for input and validates that:
    - Input contains only digits
    - Input is exactly NUMBER_LENGTH digits long
    - Input doesn't start with zero
    
    Continues prompting until valid input is received.
    
    Returns:
        list[str]: List of digits from the user's valid guess
    """
    while True:
        user_number = input(f'{'':>38}').strip()

        if not user_number.isdigit():
            print(f'\n{'NOT a number! Enter the number:'.center(CENTER_WIDTH)}')
        elif len(user_number) != NUMBER_LENGTH:
            print(f'\n{f'NOT {NUMBER_LENGTH} digits! Enter the number:'.center(CENTER_WIDTH)}')
        elif user_number.startswith('0'):
            print(f'\n{'CANNOT start with zero! Enter the number:'.center(CENTER_WIDTH)}')
        else:
            break
    return list(user_number)


def evaluate_guess(generated_number: list[str], user_number: list[str]) -> tuple[int, int]:
    """Evaluate the user's guess against the generated number.
    
    Implements the Bulls and Cows game logic:
    - Bulls: Correct digits in correct positions
    - Cows: Correct digits in wrong positions
    
    Uses a marking strategy to avoid counting digits multiple times:
    - Marked positions are replaced with empty strings
    - Checks bulls first, then cows
    
    Args:
        generated_number (list[str]): The target number to guess
        user_number (list[str]): The user's guess
        
    Returns:
        tuple[int, int]: Count of (bulls, cows)
    """
    bulls = 0 #correct number in correct position
    cows = 0 #correct number in wrong position
    generated_number_copy = generated_number.copy()

    for position in range(NUMBER_LENGTH):
        if generated_number_copy[position] == user_number[position]:
            bulls += 1
            generated_number_copy[position] = ''
            user_number[position] = ''

    for position in range(NUMBER_LENGTH):
        if user_number[position] != '' and user_number[position] in generated_number_copy:
            cows +=1
            generated_number_copy[generated_number_copy.index(user_number[position])] = ''
    return bulls,  cows


def get_plurals(bulls: int, cows: int) -> tuple[str, str]:
    """Generate plural or singular forms of 'bull' and 'cow'.
    
    Args:
        bulls (int): Number of bulls found
        cows (int): Number of cows found
        
    Returns:
        tuple[str, str]: Appropriate forms ('bull'/'bulls', 'cow'/'cows')
    """
    bulls_word = 'bull ' if bulls == 1 else 'bulls'
    cows_word = 'cow ' if cows == 1 else 'cows'
    return bulls_word, cows_word


def calculate_time(start_time: float, end_time: float) -> tuple[int, int, int]:
    """Calculate elapsed time of the game.
    
    Converts total seconds into minutes and seconds for display,
    while also returning the total time for highscore tracking.
    
    Args:
        start_time (float): Game start timestamp
        end_time (float): Game end timestamp
        
    Returns:
        tuple[int, int, int]: (minutes, seconds, total_seconds)
    """
    time_elapsed = end_time - start_time
    minutes = time_elapsed // 60
    seconds = time_elapsed % 60
    return int(minutes), int(round(seconds)), int(round(time_elapsed))


def highscore(score: int) -> list[int]:
    """Update and return the list of top scores.
    
    Maintains a file with the top 10 fastest completion times.
    Creates the highscore file and parent directories if they don't exist.
    
    Args:
        score (int): The time taken to complete the current game
        
    Returns:
        list[int]: Sorted list of top scores (lowest to highest)
        
    Note:
        Handles FileNotFoundError for first run
        Handles ValueError for corrupted score file
        Handles OSError for file permission issues
    """
    HIGHSCORE_FILE.parent.mkdir(parents=True, exist_ok=True)

    try:
        with HIGHSCORE_FILE.open('r', encoding='UTF-8') as file:
            scores = [int(line.strip()) for line in file if line.strip()]
    except (FileNotFoundError, ValueError):
        scores = []
    scores.append(score)
    scores = sorted(scores)[:10]

    try:
        with HIGHSCORE_FILE.open('w', encoding='UTF-8') as file:
            for s in scores:
                file.write(f"{s}\n")
    except OSError as e:
        print(f"Warning: Could not save highscore: {e}")
    return scores


def ask_to_continue() -> bool:
    """Prompt the user to play another round.
    
    Continuously prompts until a valid 'y' or 'n' response is received.
    Input is case-insensitive and whitespace is stripped.
    
    Returns:
        bool: True if player wants to continue, False otherwise
    """
    while True:
        answer = input(f'\n{'Play again? (y/n):'.center(CENTER_WIDTH)}\n{' ':>38}').strip().lower()
        if answer in ('y', 'n'):
            return answer == 'y'
        print(f'\n{'Please enter y or n:'.center(CENTER_WIDTH)}')


def end_credits(divider: str, mins: int, secs: int, high_scores: list[int], attempts: int) -> str:
    """Generate the end game display with statistics and high scores.
    
    Creates a formatted display showing:
    - Congratulations message
    - Time taken (in minutes and seconds)
    - Number of attempts
    - List of top scores
    
    Args:
        divider (str): String used for visual separation
        mins (int): Minutes taken to complete the game
        secs (int): Seconds taken to complete the game
        high_scores (list[int]): List of best completion times
        attempts (int): Number of guesses made
        
    Returns:
        str: Formatted end game display
    """
    minutes_label = '' if mins == 0 else f'{mins} min and '
    highscore_lines = [
        f'{i+1}. {str(score).rjust(5)} sec' for i, score in enumerate(high_scores)
    ]
    highscore_text = '\n'.join(line.center(CENTER_WIDTH)
        for line in highscore_lines)
    highscore_label = f'''
{divider}
{'CONGRATULATIONS!'.center(CENTER_WIDTH)}
{'You won in ' + f'{minutes_label}{secs} sec.':^{CENTER_WIDTH}}
{'with ' + str(attempts) + ' attempts':^{CENTER_WIDTH}}
{divider}
{'TOP SCORES'.center(CENTER_WIDTH)}
{highscore_text}
{divider}'''
    return highscore_label
