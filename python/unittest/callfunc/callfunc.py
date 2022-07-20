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

    def exitst(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

    def globalSet(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)
        changePath.classvar = dummyClass()

    def globalUnset(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)
        del changePath.classvar

class UnitTest_testModule1(unittest.TestCase):
    def setUp(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

    def tearDown(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

    def test_function1(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        _changePath = changePath()
        del _changePath

    def test_function2(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

class UnitTest_testModule2(unittest.TestCase):
    @classmethod
    def setUpClass(dummyArg):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

    @classmethod
    def tearDownClass(dummyArg):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

    def setUp(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

    def tearDown(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

    def test_function1(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

    def test_function2(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

if __name__ == '__main__':
    unittest.main()
