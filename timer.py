class Timer:
    """
    Pomodoro timer with selectable work durations and automatic break cycles.
    """

    def __init__(self):
        """
        Initializes timer state.
        """
        self.break_map = {
            25: 5,
            15: 5,
            10: 3
        }

        self.work_minutes = 25
        self.work_time = 25 * 60
        self.break_time = 5 * 60

        self.current_time = self.work_time
        self.is_break = False
        self.is_running = False

    def set_work_time(self, minutes):
        """
        Sets work duration and corresponding break time.
        """
        if minutes not in self.break_map:
            raise ValueError("Invalid selection. Choose 25, 15, or 10.")

        self.work_minutes = minutes
        self.work_time = minutes * 60
        self.break_time = self.break_map[minutes] * 60

        self.current_time = self.work_time
        self.is_break = False

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def reset(self):
        self.current_time = self.work_time
        self.is_break = False
        self.is_running = False

    def tick(self):
        if not self.is_running:
            return

        if self.current_time > 0:
            self.current_time -= 1
        else:
            self.switch_mode()

    def switch_mode(self):
        self.is_break = not self.is_break
        self.current_time = self.break_time if self.is_break else self.work_time

    def get_time(self):
        minutes = self.current_time // 60
        seconds = self.current_time % 60
        return f"{minutes:02}:{seconds:02}"

    def get_mode(self):
        return "Break" if self.is_break else "Work"
    