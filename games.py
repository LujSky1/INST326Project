import random

class Game:
    def start(self):
        raise NotImplementedError


# Tic Tac Toe (TEMP SIMPLE VERSION)

class TicTacToe(Game):
    def start(self):
        print("Tic Tac Toe launched (GUI coming soon)")


# Rock Paper Scissors
class RockPaperScissors(Game):

    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def start(self):
        print("Starting Rock Paper Scissors...")
        player_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = random.choice(self.choices)

        result = self.get_result(player_choice, computer_choice)

        print(f"Computer chose: {computer_choice}")
        print(f"Result: {result}")

    def get_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"

        if (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            return "win"

        return "lose"


# Flappy Bird (TEMP)
class FlappyBird(Game):
    def start(self):
        print("Flappy Bird launched (not implemented yet)")