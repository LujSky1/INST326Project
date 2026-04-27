import tkinter as tk

class StudyWidget:
    """
    Represents the main graphical user interface for the Study Companion Widget.

    This class is responsible for creating and managing the main window,
    displaying the timer, and handling user interactions.
    """

    def __init__(self):
        """
        Initializes the GUI window and its components.
        """
        self.root = tk.Tk()
        self.root.title("Study Widget")
        
        self.root.geometry("300x250")
        
        self.root.attributes("-topmost", True)
        
        # Timer Display
        self.timer_label = tk.Label(
            self.root,
            text="25:00",
            font=("Arial", 28)
        )
        self.timer_label.pack(pady=10)
        
        #Start Timer Buttom
        self.start_button = tk.Button(
            self.root,
            text="Start Timer",
            command=self.start_timer
        )
        self.start_button.pack(pady=5)

        #Games Section Label
        self.games_label = tk.Label(
            self.root,
            text="Break Games",
            font=("Arial", 12, "bold")
        )
        self.games_label.pack(pady=10)

        # Game Buttons
        self.ttt_button = tk.Button(
            self.root,
            text="Tic Tac Toe",
            command=self.launch_tictactoe
        )
        self.ttt_button.pack(pady=2)

        self.rps_button = tk.Button(
            self.root,
            text="Rock Paper Scissors",
            command=self.launch_rps
        )
        self.rps_button.pack(pady=2)

        self.flappy_button = tk.Button(
            self.root,
            text="Flappy Bird",
            command=self.launch_flappy
        )
        self.flappy_button.pack(pady=2)

    def start_timer(self):
        """
        Starts the timer.

        This is a placeholder method that will later connect
        to the Pomodoro timer logic.
        """
        print("Timer started!")
        
    def launch_tictactoe(self):
        """
        Launches the Tic Tac Toe game.
        """
        game = TicTacToe()
        game.start()

    def launch_rps(self):
        """
        Launches the Rock Paper Scissors game.
        """
        game = RockPaperScissors()
        game.start()

    def launch_flappy(self):
        """
        Launches the Flappy Bird game.
        """
        game = FlappyBird()
        game.start()
        
    def run(self):
        """
        Runs the main event loop for the GUI.
        """
        self.root.mainloop()
