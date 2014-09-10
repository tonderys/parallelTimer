import unittest
from timer import *

class timerTests(unittest.TestCase):
    def testNoInput(self):
        testedTimer = Timer()
        self.assertEqual(testedTimer.startTime, 0)

if __name__ == '__main__':
    unittest.main()
