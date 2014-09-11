import time

class Timer:
    def __init__(self, timeString = '0'):
        self.startTime = int(timeString)
        self.currentTime = 0
        play = False
        pause = False
        stop = True
