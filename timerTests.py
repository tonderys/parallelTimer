import unittest
from timer import *

class timerTests(unittest.TestCase):
    def testNoInput(self):
        testedTimer = Timer()
        self.assertEqual(testedTimer.getStartTime(), "00:00:00")

    def testInput(self):
        testedTimer = Timer(10)
        self.assertEqual(testedTimer.getStartTime(), "00:00:10")
        self.assertEqual(testedTimer.getCurrentTime(), "00:00:10")

    def testCurrentTimeAfterInit(self):
        testedTimer = Timer()
        self.assertEqual(testedTimer.getCurrentTime(), "00:00:00")

    def testCountDownThread(self):
        testedTimer = Timer(10)
        self.assertEqual(testedTimer.getCurrentTime(), "00:00:10")
        testedTimer.startCountDown()
        time.sleep(6)
        self.assertEqual(testedTimer.getCurrentTime(), "00:00:05")
        time.sleep(4)

    def testCountDownThreads(self):
        testedTimer1 = Timer(10)
        testedTimer2 = Timer("00:00:08")
        testedTimer1.startCountDown()
        testedTimer2.startCountDown()
        time.sleep(3)
        self.assertEqual(testedTimer1.getCurrentTime(), "00:00:08")
        self.assertEqual(testedTimer2.getCurrentTime(), "00:00:06")
        time.sleep(7)



if __name__ == '__main__':
    unittest.main()
