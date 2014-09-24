import time
import threading
import copy
from timeUnit import *

class Timer:
    def __init__(self, timeInput = '0'):
        self.startTime = timeUnit(timeInput)
        self.currentTime = timeUnit(timeInput)
        self.play = False
        self.pause = False
        self.stop = True
        self.countDownThread = threading.Thread(target = self.countDown)

    def countDown(self):
        while self.currentTime.getSeconds() > 0:
            time.sleep(1)
            self.currentTime.substractSecond()
        return True

    def startCountDown(self):
        self.play = True
        self.stop = False
        self.currentTime = copy.copy(self.startTime)
        self.countDownThread.start()

    def getStartTime(self):
        return self.startTime.getTimeString()

    def getCurrentTime(self):
        return self.currentTime.getTimeString()
