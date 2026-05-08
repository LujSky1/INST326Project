import random

class Game:
    def start(self):
        raise NotImplementedError


class TicTacToe(Game):
    def start(self):
        print("Tic Tac Toe launched (not fully implemented yet)")


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


class FlappyBird(Game):

    """ 
    base class for all mini-games. subclasses must implement start().
    """
    
    def start(self):
        """ 
        Starts the game. must be overridden by subclasses.
        """
        raise NotImplementedError ("subclasses must implement start()")

class FlappyBird(Game):
        """
        A Flappy Bird game where the bird must pass through pipes without hitting them or the ground.

        Attributes:
          bird_y (float): vertical position of the bird.
          velocity (float): current vertical speed of the bird
          score (int): number of pipes passed
          is_alive (bool): false if bird has collided
          pipes (list): list of active pipe obstacles
          """
    
        GRAVITY = 1.5
        FLAP_STRENGTH = -10
        PIPE_WIDTH = 60
        GAP_SIZE = 150
        SCREEN_HEIGHT = 600
        SCREEN_WIDTH = 400
        BIRD_X = 80
        BIRD_SIZE = 20

    def__init__(self):
    """ 
    initializes the bird position, velocity, score, and first pipe.
    """
      self.bird_y = self.SCREEN_HEIGHT // 2
      self.velocity = 0
      self.score = 0
      self.is_alive = True
      self.pipes = []
      self.generate_pipe()

   def start(self):
       """
       starts with Flappy Bird game loop.
       """
       print("Starting Flappy Bird game...")
