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
    Simple Flappy Bird game with moving pipes.
    """

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Flappy Bird")

        self.width = 400
        self.height = 500

        self.canvas = tk.Canvas(
            self.window,
            width=self.width,
            height=self.height,
            bg="skyblue"
        )
        self.canvas.pack()

        # Bird
        self.bird = self.canvas.create_oval(
            50, 200, 80, 230,
            fill="yellow"
        )

        self.velocity = 0

        # Pipe settings
        self.pipe_width = 60
        self.pipe_gap = 150

        self.pipes = []

        self.score = 0

        self.score_text = self.canvas.create_text(
            50,
            30,
            text="Score: 0",
            font=("Arial", 16, "bold")
        )

        self.create_pipe()

        self.window.bind("<space>", self.flap)

        self.update_game()

    def flap(self, event):
        """
        Makes bird jump upward.
        """
        self.velocity = -8

    def create_pipe(self):
        """
        Creates a new random pipe pair.
        """
        gap_y = random.randint(100, 300)

        top_pipe = self.canvas.create_rectangle(
            self.width,
            0,
            self.width + self.pipe_width,
            gap_y,
            fill="green"
        )

        bottom_pipe = self.canvas.create_rectangle(
            self.width,
            gap_y + self.pipe_gap,
            self.width + self.pipe_width,
            self.height,
            fill="green"
        )

        self.pipes.append((top_pipe, bottom_pipe))

    def move_pipes(self):
        """
        Moves pipes left across screen and creates new ones with spacing.
        """

        # Move all pipes
        for pipe_pair in self.pipes:
            for pipe in pipe_pair:
                self.canvas.move(pipe, -5, 0)

        # Remove pipes off screen
        if self.pipes:
            first_top_pipe = self.pipes[0][0]
            coords = self.canvas.coords(first_top_pipe)

            if coords[2] < 0:
                for pipe in self.pipes[0]:
                    self.canvas.delete(pipe)

                self.pipes.pop(0)

                self.score += 1

                self.canvas.itemconfig(
                    self.score_text,
                    text=f"Score: {self.score}"
                )

        # Create new pipe ONLY when last pipe reaches a position
        if self.pipes:
            last_pipe = self.pipes[-1][0]
            coords = self.canvas.coords(last_pipe)

            # Pipe spacing
            if coords[0] < 220:
                self.create_pipe()
        else:
            # First pipe
            self.create_pipe()

    def check_collision(self):
        """
        Checks if bird hits pipe or ground.
        """
        bird_coords = self.canvas.coords(self.bird)

        # Ground collision
        if bird_coords[3] >= self.height:
            return True

        # Ceiling collision
        if bird_coords[1] <= 0:
            return True

        # Pipe collision
        for pipe_pair in self.pipes:
            for pipe in pipe_pair:
                pipe_coords = self.canvas.coords(pipe)

                overlap = not (
                    bird_coords[2] < pipe_coords[0] or
                    bird_coords[0] > pipe_coords[2] or
                    bird_coords[3] < pipe_coords[1] or
                    bird_coords[1] > pipe_coords[3]
                )

                if overlap:
                    return True

        return False

    def update_game(self):
        """
        Main game loop.
        """
        self.velocity += 0.5

        self.canvas.move(self.bird, 0, self.velocity)

        self.move_pipes()

        if self.check_collision():
            messagebox.showinfo(
                "Game Over",
                f"Final Score: {self.score}"
            )

            self.window.destroy()
            return

        self.window.after(30, self.update_game)

    def start(self):
        self.window.mainloop()