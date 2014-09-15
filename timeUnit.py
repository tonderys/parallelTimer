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
        
    def substractSeconds(self, value = 1):
        if (self.seconds >= value):
            self.seconds -= value
        elif (self.seconds < value % 60):
            self.seconds = 60 - (value % 60 - self.seconds) 
            self.substractMinutes(1 + value // 60)
        else:
            self.seconds -= value % 60
            self.substractMinutes(value // 60)

    def substractMinutes(self, value = 1):
        if (self.minutes >= value):
            self.minutes -= value
        elif (self.minutes < value % 60):
            self.minutes = 60 - (value % 60 - self.minutes)
            self.substractHours(1 + value // 60)
        else:
            self.minutes -= value % 60
            self.substractHours(value // 60)

    def substractHours(self, value = 1):
        if self.hours - value < 0:
            self.hours = 0
        else:
            self.hours -= value
        
    def addSeconds(self, value):
        self.addMinutes((self.seconds + value) // 60)
        self.seconds = (self.seconds + value) % 60

    def addMinutes(self, value):
        self.addHours((self.minutes + value) // 60)
        self.minutes = (self.minutes + value) % 60

    def addHours(self, value):
        self.hours += value

