class Timer:
    """
    Pomodoro timer with selectable work durations and automatic break cycles.
    """

    def __init__(self):
        """
        Initializes default timer state.
        """
        self.work_durations = {
            25: 5,
            15: 5,
            10: 3
        }

        self.work_time = 25 * 60  
        self.break_time = 5 * 60

        self.current_time = self.work_time

        self.is_break = False
        self.is_running = False

    def set_work_time(self, minutes):
        """
        Sets the work and break durations.

        Args:
            minutes (int): Selected work duration (10, 15, or 25)
        """
        if minutes not in self.work_durations:
            raise ValueError("Invalid work duration selected.")

        self.work_time = minutes * 60
        self.break_time = self.work_durations[minutes] * 60
        self.current_time = self.work_time
        self.is_break = False

    def start(self):
        """
        Starts the timer.
        """
        self.is_running = True

    def stop(self):
        """
        Stops the timer.
        """
        self.is_running = False

    def reset(self):
        """
        Resets the timer to the beginning of the current work session.
        """
        self.current_time = self.work_time
        self.is_break = False
        self.is_running = False

    def tick(self):
        """
        Updates the timer by one second.

        Returns:
            int: Current time remaining in seconds.
        """
        if self.is_running:
            if self.current_time > 0:
                self.current_time -= 1
            else:
                self.switch_mode()
        return self.current_time

    def switch_mode(self):
        """
        Switches between work and break sessions.
        """
        self.is_break = not self.is_break

        if self.is_break:
            self.current_time = self.break_time
        else:
            self.current_time = self.work_time

    def get_time(self):
        """
        Returns formatted time string.

        Returns:
            str: Time in MM:SS format.
        """
        minutes = self.current_time // 60
        seconds = self.current_time % 60
        return f"{minutes:02}:{seconds:02}"

    def get_mode(self):
        """
        Returns current mode as string.

        Returns:
            str: "Work" or "Break"
        """
        return "Break" if self.is_break else "Work"