#Editing tic-tac-toe game - YPL
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
###### Additional code pending edits
class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.board = [" "] * 9
        self.current_player = "X" #Human player = X, Computer player = random
        self.buttons = []
        self._setup_ui()

    def _setup_ui(self):
        for i in range(9):
            button = tk.Button(self.window, text="", font=('normal', 20), width=5, height=2,
                               command=lambda i=i: self.human_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def human_move(self, index):
        if self.board[index] == " " and self.current_player == "X":
            self.make_move(index, "X")
            if not self.check_game_over():
                self.window.after(500, self.computer_move) # Delay computer move slightly


    def computer_move(self):
        empty_slots = [i for i, spot in enumerate(self.board) if spot == " "]
        if empty_slots:
            index = random.choice(empty_slots)
            self.make_move(index, "O")
            self.check_game_over()

    def make_move(self, index, player):
        self.board[index] = player
        self.buttons[index].config(text=player, state="disabled", disabledforeground="black")
        self.current_player = "O" if player == "X" else "X"

def check_game_over(self):
        win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        
        for combo in win_conditions:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                messagebox.showinfo(f"Player {self.board[combo[0]]} wins!")
                self.window.quit()
                return True
        
        if " " not in self.board:
            messagebox.showinfo("It's a tie!")
            self.window.quit()
            return True
        return False

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
######

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

import random

class RockPaperScissors(Game):
    """
    Implements Rock Paper Scissors game.

    The player selects an option and the computer randomly selects one.
    The result is calculated based on standard game rules.
    """

    def __init__(self):
        """
        Initializes the game with available choices.
        """
        self.choices = ["rock", "paper", "scissors"]

    def start(self):
        """
        Starts the game in command-line mode (for testing).
        """
        print("Starting Rock Paper Scissors...")
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = self.get_computer_choice()

        result = self.get_result(player_choice, computer_choice)

        print(f"Computer chose: {computer_choice}")
        print(f"Result: {result}")

    def get_computer_choice(self):
        """
        Randomly selects a choice for the computer.

        Returns:
            str: computer's choice
        """
        return random.choice(self.choices)

    def get_result(self, player_choice, computer_choice):
        """
        Determines the result of the game.

        Args:
            player_choice (str): Player's choice
            computer_choice (str): Computer's choice

        Returns:
            str: "win", "lose", or "tie"
        """
        if player_choice == computer_choice:
            return "tie"

        if (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            return "win"

        return "lose"

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
