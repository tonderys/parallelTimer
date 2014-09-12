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

    def getTime(self):
        return "%02d:%02d:%02d"%(self.hours, self.minutes, self.seconds)

    def setTime(self, time):
        if re.match("[0-9]{2}:[0-9]{2}:[0-9]{2}", time):
            self.hours = int(time.split(':')[0])
            self.minutes = int(time.split(':')[1])
            self.seconds = int(time.split(':')[2])
        elif re.match("[0-9]*", time):
            self.setSeconds(int(time))
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        
    def setSeconds(self, time):
        self.hours = time // 3600
        self.minutes = (time % 3600) // 60
        self.seconds = time % 60
        
    def substractSeconds(self, value = 1):
        self.seconds -= value

    def substractMinutes(self, value = 1):
        self.minutes -= value

    def substractHours(self, value = 1):
        self.hours -= value
        
    def addSeconds(self, value):
        self.seconds += value

    def addMinutes(self, value):
        self.minutes += value

    def addHours(self, value):
        self.hours += value

