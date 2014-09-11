class timeUnit:
    def __init__(self, time = 0):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def getTime(self):
        time = ""
        if self.hours < 10:
            time +='0'+ str(self.hours)+":"
        else:
            time += str(self.hours)+":"
        if self.minutes < 10:
            time +='0'+ str(self.minutes)+":"
        else:
            time += str(self.minutes)+":"
        if self.seconds < 10:
            time +='0'+ str(self.seconds)
        else:
            time += str(self.seconds)
        return time
