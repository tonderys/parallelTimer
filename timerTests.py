import unittest
from timer import *

class timerTests(unittest.TestCase):
    def testNoInput(self):
        testedTimer = Timer()
        self.assertEqual(testedTimer.getStartTime(), 0)

    def testInputString0(self):
        testedTimer = Timer('0')
        self.assertEqual(testedTimer.getStartTime(), 0)

    def testInputString1(self):
        testedTimer = Timer('1')
        self.assertEqual(testedTimer.getStartTime(), 1)

    def testInputWithMinutes(self):
        testedTimer = Timer('0:01')
        self.assertEqual(testedTimer.getStartTime(), 1)
if __name__ == '__main__':
    unittest.main()
