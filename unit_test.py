import unittest
import tkinter as tk
from games import RockPaperScissors, TicTacToe, FlappyBird
from timer import Timer



class TestRockPaperScissors(unittest.TestCase):
    """
    Unit tests for RockPaperScissors class.
    """

    def setUp(self):
        """
        Creates a new game instance before each test.
        """
        self.game = RockPaperScissors()

    def test_tie(self):
        """
        Tests that identical choices result in a tie.
        """
        self.assertEqual(self.game.get_result("rock", "rock"), "tie")

    def test_player_win_cases(self):
        """
        Tests all winning scenarios for the player.
        """
        self.assertEqual(self.game.get_result("rock", "scissors"), "win")
        self.assertEqual(self.game.get_result("paper", "rock"), "win")
        self.assertEqual(self.game.get_result("scissors", "paper"), "win")

    def test_player_lose_cases(self):
        """
        Tests all losing scenarios for the player.
        """
        self.assertEqual(self.game.get_result("rock", "paper"), "lose")
        self.assertEqual(self.game.get_result("paper", "scissors"), "lose")
        self.assertEqual(self.game.get_result("scissors", "rock"), "lose")


class TestTicTacToe(unittest.TestCase):
    """
    Unit tests for TicTacToe class.
    """

    def setUp(self):
        self.game = TicTacToe()

    def test_board_initialization(self):
        """
        Board should start empty.
        """
        self.assertEqual(len(self.game.board), 9)
        self.assertTrue(all(cell == " " for cell in self.game.board))

    def test_make_move(self):
        """
        Test that a move updates the board.
        """
        self.game.make_move(0)
        self.assertNotEqual(self.game.board[0], " ")

    def test_switch_player(self):
        """
        Test that player switches correctly.
        """
        first = self.game.current_player
        self.game.switch_player()
        self.assertNotEqual(first, self.game.current_player)

class TestFlappyBird(unittest.TestCase):
    """
    Unit tests for FlappyBird class.
    """

    def setUp(self):
        """
        Creates a hidden tkinter window and new FlappyBird instance before each test.
        """
        self.root = tk.Tk()
        self.root.withdraw()
        self.game = FlappyBird()

    def tearDown(self):
        """
        destroys the window after each test.
        """
        self.game.window.destroy()
        self.root.destroy()

    def test_score_starts_at_zero(self):
        """
        score should be 0 at the start.
        """
        self.assertEqual(self.game.score, 0)

    def test_velocity_starts_at_zero(self):
        """
        velocity should be at 0 at the start.
        """
        self.assertEqual(self.game.velocity, 0)

    def test_pipes_not_empty(self):
        """
        at least one pipe should exist at the start of the game
        """
        self.assertGreaterEqual(len(self.game.pipes), 1)

    def test_flap_sets_negative_velocity(self):
        """
        flap should set velocity to -8
        """
        self.game.flap(None)
        self.assertEqual(self.game.velocity, -8)

    def test_no_collision_at_start(self):
        """
        the bird should not collide at the starting position
        """
        self.game.pipes = []
        self.assertFalse(self.game.check_collision())
        

class TestTimer(unittest.TestCase):

    def setUp(self):
        self.timer = Timer()  # small values for testing

    def test_initial_state(self):
        self.assertEqual(self.timer.work_minutes, 25)
        self.assertEqual(self.timer.current_time, 1500)
        self.assertFalse(self.timer.is_break)
        self.assertFalse(self.timer.is_running)

    def test_start(self):
        self.timer.start()
        self.assertTrue(self.timer.is_running)

    def test_stop(self):
        self.timer.start()
        self.timer.stop()
        self.assertFalse(self.timer.is_running)

    def test_tick(self):
        self.timer.start()
        initial = self.timer.current_time
        self.timer.tick()
        self.assertEqual(self.timer.current_time, initial - 1)

    def test_switch_mode(self):
        self.timer.current_time = 0
        self.timer.start()
        self.timer.tick()
        self.assertTrue(self.timer.is_break)
        self.assertEqual(self.timer.get_mode(), "Break")

    def test_format_time(self):
        self.timer.current_time = 65
        self.assertEqual(self.timer.get_time(), "01:05")

    def test_set_work_time(self):
        self.timer.set_work_time(15)
        self.assertEqual(self.timer.work_minutes, 15)
        self.assertEqual(self.timer.current_time, 900)
        self.assertEqual(self.timer.break_time, 300)

    def test_invalid_work_time(self):
        with self.assertRaises(ValueError):
            self.timer.set_work_time(20)

if __name__ == "__main__":
    unittest.main()
