import unittest
from timeUnit import *

class timeUnitTests(unittest.TestCase):
    def testNoInput(self):
        testedTimeUnit = timeUnit()
        self.assertEqual(testedTimeUnit.getTime(), '00:00:00')

    def testInput0Seconds(self):
        testedTimeUnit = timeUnit('0')
        self.assertEqual(testedTimeUnit.getTime(), '00:00:00')

if __name__ == '__main__':
    unittest.main()
