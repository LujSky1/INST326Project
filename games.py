"""
This module contains all mini-games used in the Study Companion Desktop Widget.

Each game is implemented as a class with its own logic and can be launched
independently from the main GUI. The games are designed to run during
Pomodoro break periods to provide short interactive entertainment.
"""

class Game:
    """
    Base class for all games in the project.

    This class defines a standard structure that all games should follow,
    making it easier to integrate them into the main widget system.
    """

    def start(self):
        """
        Starts the game.
        Must be implemented by all child classes.
        """
        raise NotImplementedError("Each game must implement a start method.")


class TicTacToe(Game):
    """
    Implements a simple Tic Tac Toe game.

    This game allows two players
    to take turns marking a 3x3 grid until one player wins or the game ties.
    """

    def __init__(self):
        """
        Initializes the game board and sets the starting player.
        """

    def start(self):
        """
        Starts the Tic Tac Toe game loop.
        """
        print("Starting Tic Tac Toe game...")

    def make_move(self, position):
        """
        Places the current player's mark on the board.

        Args:
            position (int): Board position (0-8)
        """
    
    def switch_player(self):
        """
        Switches turns between player X and O.
        """

class RockPaperScissors(Game):
    """
    Implements Rock Paper Scissors game.

    The player chooses an option and the computer randomly selects one.
    The winner is determined based on standard rules.
    """

    def __init__(self):
        """
        Initializes available choices.
        """

    def start(self):
        """
        Starts the Rock Paper Scissors game.
        """
        print("Starting Rock Paper Scissors...")

    def get_result(self, player_choice, computer_choice):
        """
        Determines the result of the game.

        Args:
            player_choice (str): Player's selection
            computer_choice (str): Computer's selection

        Returns:
            str: result of the game (win/lose/tie)
        """

class FlappyBird(Game):
    """
    Simplified Flappy Bird-style game.

    """

    def __init__(self):
        """
        Initializes game variables.
        """
     

    def start(self):
        """
        Starts the Flappy Bird game loop.
        """
        print("Starting Flappy Bird game...")

    def flap(self):
        """
        Moves bird upward by flapping (clicking) the wings.
        """


    def gravity(self):
        """
        Simulates gravity pulling the bird downward.
        """
