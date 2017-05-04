import time


class Stopwatch:
    """Counts the past time"""

    def __init__(self):
        self.__beginning = None
        self.__end = 0.0

    def start(self):
        """Starts the timer"""
        self.__beginning = time.time()

    def stop(self):
        """Stops the timer. returns time in seconds"""
        self.__end = time.time() - self.__beginning
        return self.get_stopped_time()

    def get_stopped_time(self):
        """returns last stopped time in seconds"""
        return round(self.__end, 3)
