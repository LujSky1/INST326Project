import unittest
from timer import Timer

class TestTimer(unittest.TestCase):
    """
    Unit tests for the Timer class.
    """

    def test_initialization(self):
        """
        Tests that the timer initializes with correct values.
        """
        timer = Timer(25, 5)
        self.assertEqual(timer.work_time, 25)
        self.assertEqual(timer.break_time, 5)

    def test_switch_mode(self):
        """
        Tests switching between work and break modes.
        """
        timer = Timer(25, 5)
        timer.switch_mode()
        self.assertTrue(timer.is_break)
        self.assertEqual(timer.current_time, 5)

    def test_tick(self):
        """
        Tests that the timer decreases correctly.
        """
        timer = Timer(25, 5)
        timer.tick()
        self.assertEqual(timer.current_time, 24)

if __name__ == "__main__":
    unittest.main()