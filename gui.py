import tkinter as tk
from timer import Timer
from games import TicTacToe, RockPaperScissors, FlappyBird

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
        
        self.timer = Timer()
        
        self.root.geometry("300x250")
        
        self.root.attributes("-topmost", True)

        self.selected_time = tk.IntVar(value=25)

        self.dropdown = tk.OptionMenu(
            self.root,
            self.selected_time,
                25, 15, 10
                )
        self.dropdown.pack(pady=5)
        
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

        self.stop_button = tk.Button(
            self.root,
            text="Stop Timer",
            command=self.stop_timer
            )
        self.stop_button.pack(pady=5)

    def start_timer(self):
        """
        Starts the timer and begins updating the display.
        """
        selected = self.selected_time.get()
        self.timer.set_work_time(selected)
        self.timer.start()
        self.update_timer()
        
    def launch_tictactoe(self):
        """
        Launches the Tic Tac Toe game.
        """
        game = TicTacToe()
        game.start()
        
    def update_timer(self):
        """
        Updates the timer display every second.
        """
        self.timer.tick()
        self.timer_label.config(text=self.timer.get_time())

        if self.timer.is_running:
            self.root.after(1000, self.update_timer)

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
