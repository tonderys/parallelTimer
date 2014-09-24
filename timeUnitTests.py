import unittest
from timeUnit import *

class timeUnitInputTests(unittest.TestCase):
    def testNoInput(self):
        testedTimeUnit = timeUnit()
        self.assertEqual(testedTimeUnit.getTimeString(), '00:00:00')
        self.assertEqual(testedTimeUnit.getSeconds(), 0)

    def testInputSeconds(self):
        testedTimeUnit = timeUnit(10)
        self.assertEqual(testedTimeUnit.getTimeString(), '00:00:10')
        self.assertEqual(testedTimeUnit.getSeconds(), 10)

    def testInputMoreThan60Seconds(self):
        testedTimeUnit = timeUnit(60 + 1)
        self.assertEqual(testedTimeUnit.getTimeString(), '00:01:01')
        self.assertEqual(testedTimeUnit.getSeconds(), 61)

    def testInputMoreThan3600Seconds(self):
        testedTimeUnit = timeUnit(3600*2 + 60*3 + 4)
        self.assertEqual(testedTimeUnit.getTimeString(), '02:03:04')
        self.assertEqual(testedTimeUnit.getSeconds(), 3600*2 + 60*3 + 4)

    def testInputFullTimeAllZeros(self):
        testedTimeUnit = timeUnit('00:00:00')
        self.assertEqual(testedTimeUnit.getTimeString(), '00:00:00')

    def testInputFullTimeOnlySeconds(self):
        testedTimeUnit = timeUnit('00:00:15')
        self.assertEqual(testedTimeUnit.getTimeString(), '00:00:15')

    def testInputFullTimeOnlyMinutes(self):
        testedTimeUnit = timeUnit('00:13:00')
        self.assertEqual(testedTimeUnit.getTimeString(), '00:13:00')

    def testInputFullTimeOnlyHours(self):
        testedTimeUnit = timeUnit('24:00:00')
        self.assertEqual(testedTimeUnit.getTimeString(), '24:00:00')

    def testInputFullTimeMixedInput(self):
        testedTimeUnit = timeUnit('02:23:07')
        self.assertEqual(testedTimeUnit.getTimeString(), '02:23:07')

    def testInvalidInputFullTimeSeconds(self):
        testedTimeUnit = timeUnit('02:14:81')
        self.assertEqual(testedTimeUnit.getTimeString(), '00:00:00')
 
    def testInvalidInputFullTimeMinutes(self):
        testedTimeUnit = timeUnit('02:74:11')
        self.assertEqual(testedTimeUnit.getTimeString(), '00:00:00')

class timeUnitFunctionsTests(unittest.TestCase):
    
    def testSubstractSecond(self):
        testedTimeUnit = timeUnit('00:00:11')
        testedTimeUnit.substractSecond()
        self.assertEqual(testedTimeUnit.getSeconds(), 10)

    def testSubstractMinute(self):
        testedTimeUnit = timeUnit('00:02:00')
        testedTimeUnit.substractSecond()
        self.assertEqual(testedTimeUnit.getTimeString(), '00:01:59')
        self.assertEqual(testedTimeUnit.getSeconds(), 119)

    def testSubstractHour(self):
        testedTimeUnit = timeUnit('02:00:00')
        testedTimeUnit.substractSecond()
        self.assertEqual(testedTimeUnit.getTimeString(), '01:59:59')
        self.assertEqual(testedTimeUnit.getSeconds(), 3600 + 59 * 60 + 59)
if __name__ == '__main__':
    unittest.main()
