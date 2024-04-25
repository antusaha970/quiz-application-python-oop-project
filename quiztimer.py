import threading


class QuizTimer:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.time_up = False

    def start_timer(self):
        timer_thread = threading.Thread(target=self.run_timer)
        timer_thread.start()

    def run_timer(self):
        import time
        time.sleep(self.time_limit)
        self.time_up = True

    def is_time_up(self):
        return self.time_up
