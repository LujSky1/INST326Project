class Timer:
    def __init__(self, work_time, break_time):
        self.work_time = work_time * 60
        self.break_time = break_time * 60
        self.current_time = self.work_time
        self.is_break = False
        self.is_running = False

    def start(self):
        self.is_running = True

    def switch_mode(self):
        self.is_break = not self.is_break
        if self.is_break:
            self.current_time = self.break_time
        else:
            self.current_time = self.work_time

    def tick(self):
        if self.is_running:
            if self.current_time > 0:
                self.current_time -= 1
            else:
                self.switch_mode()
        return self.current_time

    def get_time(self):
        minutes = self.current_time // 60
        seconds = self.current_time % 60
        return f"{minutes:02}:{seconds:02}"