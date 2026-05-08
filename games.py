import tkinter as tk
from tkinter import messagebox
import random


class Game:
    """
    Base class for all games.
    """

    def start(self):
        raise NotImplementedError


# ==================================================
# TIC TAC TOE
# ==================================================
class TicTacToe(Game):
    """
    Simple Tic Tac Toe game against computer.
    """

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Tic Tac Toe")

        self.board = [" "] * 9
        self.current_player = "X"
        self.buttons = []

        self.setup_ui()

    def setup_ui(self):
        """
        Creates board buttons.
        """
        for i in range(9):
            button = tk.Button(
                self.window,
                text="",
                width=6,
                height=3,
                font=("Arial", 18),
                command=lambda i=i: self.human_move(i)
            )

            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def human_move(self, index):
        """
        Handles player move.
        """
        if self.board[index] == " ":
            self.make_move(index, "X")

            if not self.check_game_over():
                self.window.after(500, self.computer_move)

    def computer_move(self):
        """
        Random computer move.
        """
        empty = [i for i, spot in enumerate(self.board) if spot == " "]

        if empty:
            move = random.choice(empty)
            self.make_move(move, "O")
            self.check_game_over()

    def make_move(self, index, player):
        """
        Updates board.
        """
        self.board[index] = player
        self.buttons[index].config(text=player, state="disabled")

    def check_game_over(self):
        """
        Checks winner or tie.
        """
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]

        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                messagebox.showinfo("Winner", f"Player {self.board[a]} wins!")
                self.window.destroy()
                return True

        if " " not in self.board:
            messagebox.showinfo("Tie", "It's a tie!")
            self.window.destroy()
            return True

        return False

    def start(self):
        """
        Starts game.
        """
        self.window.mainloop()


# ==================================================
# ROCK PAPER SCISSORS
# ==================================================
class RockPaperScissors(Game):

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Rock Paper Scissors")

        self.label = tk.Label(
            self.window,
            text="Choose Rock, Paper, or Scissors",
            font=("Arial", 14)
        )
        self.label.pack(pady=10)

        for choice in ["Rock", "Paper", "Scissors"]:
            button = tk.Button(
                self.window,
                text=choice,
                width=15,
                command=lambda c=choice.lower(): self.play(c)
            )
            button.pack(pady=5)

    def play(self, player_choice):
        """
        Plays one round.
        """
        computer_choice = random.choice(
            ["rock", "paper", "scissors"]
        )

        result = self.get_result(player_choice, computer_choice)

        messagebox.showinfo(
            "Result",
            f"You chose {player_choice}\n"
            f"Computer chose {computer_choice}\n\n"
            f"You {result}!"
        )

    def get_result(self, player, computer):
        """
        Determines winner.
        """
        if player == computer:
            return "tie"

        if (
            (player == "rock" and computer == "scissors") or
            (player == "paper" and computer == "rock") or
            (player == "scissors" and computer == "paper")
        ):
            return "win"

        return "lose"

    def start(self):
        self.window.mainloop()


# ==================================================
# FLAPPY BIRD (SIMPLE VERSION)
# ==================================================
class FlappyBird(Game):
    """
    Simplified Flappy Bird animation.
    """

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Flappy Bird")

        self.canvas = tk.Canvas(
            self.window,
            width=400,
            height=500,
            bg="skyblue"
        )
        self.canvas.pack()

        self.bird = self.canvas.create_oval(
            50, 200, 80, 230,
            fill="yellow"
        )

        self.velocity = 0

        self.window.bind("<space>", self.flap)

        self.update_game()

    def flap(self, event):
        """
        Makes bird jump.
        """
        self.velocity = -8

    def update_game(self):
        """
        Updates bird movement.
        """
        self.velocity += 0.5

        self.canvas.move(self.bird, 0, self.velocity)

        pos = self.canvas.coords(self.bird)

        if pos[3] >= 500:
            messagebox.showinfo("Game Over", "Bird crashed!")
            self.window.destroy()
            return

        self.window.after(30, self.update_game)

    def start(self):
        self.window.mainloop()