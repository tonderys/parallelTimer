import unittest
from timeUnit import *

class timeUnitTests(unittest.TestCase):
    def testNoInput(self):
        testedTimeUnit = timeUnit()
        self.assertEqual(testedTimeUnit.getTime(), '00:00:00')

    def testInput0Seconds(self):
        testedTimeUnit = timeUnit('0')
        self.assertEqual(testedTimeUnit.getTime(), '00:00:00')

    def testInputSeconds(self):
        testedTimeUnit = timeUnit(10)
        self.assertEqual(testedTimeUnit.getTime(), '00:00:10')

    def testInputMoreThan60Seconds(self):
        testedTimeUnit = timeUnit(60 + 1)
        self.assertEqual(testedTimeUnit.getTime(), '00:01:01')

    def testInputMoreThan3600Seconds(self):
        testedTimeUnit = timeUnit(3600*2 + 60*3 + 4)
        self.assertEqual(testedTimeUnit.getTime(), '02:03:04')

    def testInputFullTimeAllZeros(self):
        testedTimeUnit = timeUnit('00:00:00')
        self.assertEqual(testedTimeUnit.getTime(), '00:00:00')

    def testInputFullTimeOnlySeconds(self):
        testedTimeUnit = timeUnit('00:00:15')
        self.assertEqual(testedTimeUnit.getTime(), '00:00:15')

    def testInputFullTimeOnlyMinutes(self):
        testedTimeUnit = timeUnit('00:13:00')
        self.assertEqual(testedTimeUnit.getTime(), '00:13:00')

    def testInputFullTimeOnlyHours(self):
        testedTimeUnit = timeUnit('24:00:00')
        self.assertEqual(testedTimeUnit.getTime(), '24:00:00')

    def testInputFullTimeMixedInput(self):
        testedTimeUnit = timeUnit('02:23:07')
        self.assertEqual(testedTimeUnit.getTime(), '02:23:07')

    def testSubstractSecondsFunction(self):
        testedTimeUnit = timeUnit('02:23:07')
        testedTimeUnit.substractSeconds(3)
        self.assertEqual(testedTimeUnit.getTime(), '02:23:04')

    def testSubstractMinutesFunction(self):
        testedTimeUnit = timeUnit('02:23:07')
        testedTimeUnit.substractMinutes(4)
        self.assertEqual(testedTimeUnit.getTime(), '02:19:07')

    def testSubstractHoursFunction(self):
        testedTimeUnit = timeUnit('02:23:07')
        testedTimeUnit.substractHours(2)
        self.assertEqual(testedTimeUnit.getTime(), '00:23:07')

    def SubstractSecondsFunctionExceedingSecondsQuantity(self):
        testedTimeUnit = timeUnit('02:23:07')
        testedTimeUnit.substractSeconds(9)
        self.assertEqual(testedTimeUnit.getTime(), '02:22:58')

    def SubstractMinutesFunctionExceedingMinutesQuantity(self):
        testedTimeUnit = timeUnit('02:23:07')
        testedTimeUnit.substractSeconds(33)
        self.assertEqual(testedTimeUnit.getTime(), '01:50:07')

    def InvalidInputFullTimeSeconds(self):
        testedTimeUnit = timeUnit('02:14:81')
        self.assertEqual(testedTimeUnit.getTime(), '00:00:00')

    def InvalidInputFullTimeMinutes(self):
        testedTimeUnit = timeUnit('02:74:11')
        self.assertEqual(testedTimeUnit.getTime(), '00:00:00')

if __name__ == '__main__':
    unittest.main()
