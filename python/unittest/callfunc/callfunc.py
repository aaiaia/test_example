import sys
import unittest

class dummyClass():
    def __init__(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

    def __del__(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

class changePath():
    classvar = None

    def __init__(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)
        self.objectVar = dummyClass()

    def __del__(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)
        del self.objectVar

    def exitst():
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

    def globalSet():
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)
        changePath.classvar = dummyClass()

    def globalUnset():
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)
        del changePath.classvar

class UnitTest_testModule1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_function1(self):
        _changePath = changePath()
        del _changePath

    def test_function2(self):
        pass

class UnitTest_testModule2(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_function1(self):
        pass

    def test_function2(self):
        pass

if __name__ == '__main__':
    unittest.main()
