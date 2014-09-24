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

if __name__ == '__main__':
    unittest.main()
