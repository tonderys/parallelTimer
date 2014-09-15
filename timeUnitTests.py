import unittest
from timeUnit import *

class timeUnitInputTests(unittest.TestCase):
    def testNoInput(self):
        testedTimeUnit = timeUnit()
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

    def testInvalidInputFullTimeSeconds(self):
        testedTimeUnit = timeUnit('02:14:81')
        self.assertEqual(testedTimeUnit.getTime(), '00:00:00')
 
    def testInvalidInputFullTimeMinutes(self):
        testedTimeUnit = timeUnit('02:74:11')
        self.assertEqual(testedTimeUnit.getTime(), '00:00:00')

class timeUnitFunctionsTests(unittest.TestCase):
    def setUp(self):
        self.testedTimeUnit = timeUnit('02:23:07')
        
    def testSubstractSecondsFunction(self):
        self.testedTimeUnit.substractSeconds(3)
        self.assertEqual(self.testedTimeUnit.getTime(), '02:23:04')

    def testSubstractSecondsFunctionExceedingSecondsQuantity(self):
        self.testedTimeUnit.substractSeconds(9)
        self.assertEqual(self.testedTimeUnit.getTime(), '02:22:58')
 
    def testSubstractSecondsFunctionThreeMinutes(self):
        self.testedTimeUnit.substractSeconds(60 * 3)
        self.assertEqual(self.testedTimeUnit.getTime(), '02:20:07')
 
    def testSubstractSecondsFunctionMoreThanMinute(self):
        self.testedTimeUnit.substractSeconds(64)
        self.assertEqual(self.testedTimeUnit.getTime(), '02:22:03')
 
    def testSubstractMinutesFunction(self):
        self.testedTimeUnit.substractMinutes(4)
        self.assertEqual(self.testedTimeUnit.getTime(), '02:19:07')

    def testSubstractMinutesFunctionExceedingMinutesQuantity(self):
        self.testedTimeUnit.substractMinutes(33)
        self.assertEqual(self.testedTimeUnit.getTime(), '01:50:07')
 
    def testSubstractMinutesFunctionTwoHours(self):
        self.testedTimeUnit.substractMinutes(2 * 60)
        self.assertEqual(self.testedTimeUnit.getTime(), '00:23:07')
 
    def testSubstractMinutesFunctionMoreThanHour(self):
        self.testedTimeUnit.substractMinutes(66)
        self.assertEqual(self.testedTimeUnit.getTime(), '01:17:07')
 
    def testSubstractHoursFunction(self):
        self.testedTimeUnit.substractHours(2)
        self.assertEqual(self.testedTimeUnit.getTime(), '00:23:07')

    def testSubstractSecondMethodAllSeconds(self):
        self.testedTimeUnit.substractSeconds(2 * 3600 + 23 * 60 + 7)
        self.assertEqual(self.testedTimeUnit.getTime(), '00:00:00')

    def testAddSecondsFunction(self):
        self.testedTimeUnit.addSeconds(14)
        self.assertEqual(self.testedTimeUnit.getTime(), '02:23:21')

    def testAddSecondsFunctionExceedingSecondsCapacity(self):
        self.testedTimeUnit.addSeconds(59)
        self.assertEqual(self.testedTimeUnit.getTime(), '02:24:06')

    def testAddSecondsFunctionUpToTwoMinutes(self):
        self.testedTimeUnit.addSeconds(60 + 53)
        self.assertEqual(self.testedTimeUnit.getTime(), '02:25:00')

    def testAddMinutesFunction(self):
        self.testedTimeUnit.addMinutes(8)
        self.assertEqual(self.testedTimeUnit.getTime(), '02:31:07')

    def testAddMinutesFunctionExceedingMinutesCapacity(self):
        self.testedTimeUnit.addMinutes(41)
        self.assertEqual(self.testedTimeUnit.getTime(), '03:04:07')

    def testAddMinutesFunctionUpToTwoHours(self):
        self.testedTimeUnit.addMinutes(60 + 37)
        self.assertEqual(self.testedTimeUnit.getTime(), '04:00:07')

if __name__ == '__main__':
    unittest.main()
