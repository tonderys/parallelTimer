import re

class timeUnit:
    def __init__(self, time = '0'):
        if type(time) == type('0'):
            self.setTime(time)
        elif type(time) == type(0):
            self.setSeconds(time)
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    def setTime(self, time):
        if re.match("[0-9]{2}:[0-5][0-9]:[0-5][0-9]", time):
            self.hours = int(time.split(':')[0])
            self.minutes = int(time.split(':')[1])
            self.seconds = int(time.split(':')[2])
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        
    def setSeconds(self, time):
        self.hours = time // 3600
        self.minutes = (time % 3600) // 60
        self.seconds = time % 60
        
    def getTimeString(self):
        return "%02d:%02d:%02d"%(self.hours, self.minutes, self.seconds)

    def getSeconds(self):
        return self.seconds + self.minutes * 60 + self.hours * 3600

    def substractSecond(self):
        if self.seconds > 0:
            self.seconds -= 1
        elif self.minutes > 0: 
            self.minutes -= 1
            self.seconds = 59
        elif self.hours > 0:
            self.hours -= 1
            self.minutes = 59
            self.seconds = 59
