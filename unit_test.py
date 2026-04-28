import unittest
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
        Creates a new FlappyBird instance before each test.
        """
        self.game = FlappyBird()

    def test_initial_state(self):
        """
        Tests initial values of the game.
        """
        self.assertEqual(self.game.score, 0)
        self.assertTrue(self.game.is_alive)
        self.assertEqual(self.game.position, 0)

    def test_flap(self):
        """
        Tests that flap increases position.
        """
        self.game.flap()
        self.assertEqual(self.game.position, 2)

    def test_gravity(self):
        """
        Tests that gravity decreases position.
        """
        self.game.position = 5
        self.game.gravity()
        self.assertEqual(self.game.position, 4)

    def test_game_over(self):
        """
        Tests that the game ends when position goes below zero.
        """
        self.game.position = 0
        self.game.gravity()
        self.assertFalse(self.game.is_alive)


if __name__ == "__main__":
    unittest.main()
    unittest.main()

class TestTimer(unittest.TestCase):

    def setUp(self):
        self.timer = Timer(1, 1)  # small values for testing

    def test_initial_state(self):
        self.assertFalse(self.timer.is_break)
        self.assertFalse(self.timer.is_running)

    def test_start(self):
        self.timer.start()
        self.assertTrue(self.timer.is_running)

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

    def test_format_time(self):
        self.timer.current_time = 65
        self.assertEqual(self.timer.get_time(), "01:05")


if __name__ == "__main__":
    unittest.main()