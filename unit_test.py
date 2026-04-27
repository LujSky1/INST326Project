import unittest
from games import RockPaperScissors, TicTacToe, Flappy Bird


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


if __name__ == "__main__":
    unittest.main()
    unittest.main()
