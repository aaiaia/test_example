import sys
import unittest
from unittest.mock import patch, MagicMock

import tested_code

from pathlib import Path

class replace_path_library():
    truepath = ''

    def __init__(self, filepath):
        self.filepath = filepath

    def set_truepath(filepath):
        replace_path_library.truepath = filepath

    def exists(self):
        if self.filepath == replace_path_library.truepath:
            return True
        else:
            return False

class Test_changeFunction0(unittest.TestCase):
    def setUp(self):
        replace_path_library.set_truepath('')

    def tearDown(self):
        replace_path_library.set_truepath('')

    @patch('tested_code.Path')
    def test_0000_PathLibMockingUsingPatch_notExist(self, path_mock):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        path_mock.side_effect = replace_path_library  # replace to class

        # set changed Path library True case, Path().exist()
        replace_path_library.set_truepath('')

        #replace_path_library.set_truepath(_pre_wavepath)  # set true path
        tested_code.packageFunction()

    @patch('tested_code.Path')
    def test_0001_PathLibMockingUsingPatch_exist(self, path_mock):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        path_mock.side_effect = replace_path_library  # replace to class

        # declare variables
        _filePath = 'mockingFileLoc.log'
        # set changed Path library True case, Path().exist()
        replace_path_library.set_truepath(_filePath)

        #replace_path_library.set_truepath(_pre_wavepath)  # set true path
        tested_code.packageFunction(_filePath)

    def test_0002_call_packageFunction(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        tested_code.packageFunction()

    def test_0003_overwritePathLibToTrue(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        Path.exists=MagicMock(return_value=True)

        tested_code.packageFunction()

    def test_0004_overwritePathLibToFalse(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        Path.exists=MagicMock(return_value=False)

        tested_code.packageFunction()

    def test_0005_overwritePathLibToTrue(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        Path.exists=MagicMock(return_value=True)

        tested_code.packageFunction()

    def test_0006_justRunPackageFunction(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        tested_code.packageFunction()

    def test_0007_justRunPackageFunction(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        tested_code.packageFunction()

class Test_changeFunction1(unittest.TestCase):
    def setUp(self):
        replace_path_library.set_truepath('')

    def tearDown(self):
        replace_path_library.set_truepath('')

    @patch('tested_code.Path')
    def test_0000_PathLibMockingUsingPatch_notExist(self, path_mock):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        path_mock.side_effect = replace_path_library  # replace to class

        # set changed Path library True case, Path().exist()
        replace_path_library.set_truepath('')

        #replace_path_library.set_truepath(_pre_wavepath)  # set true path
        tested_code.packageFunction()

    @patch('tested_code.Path')
    def test_0001_PathLibMockingUsingPatch_exist(self, path_mock):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        path_mock.side_effect = replace_path_library  # replace to class

        # declare variables
        _filePath = 'mockingFileLoc.log'
        # set changed Path library True case, Path().exist()
        replace_path_library.set_truepath(_filePath)

        #replace_path_library.set_truepath(_pre_wavepath)  # set true path
        tested_code.packageFunction(_filePath)

    def test_0002_justRunPackageFunction(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        tested_code.packageFunction()

    def test_0003_justRunPackageFunction(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        tested_code.packageFunction()

    def test_0004_justRunPackageFunction(self):
        _funcName = sys._getframe(0).f_code.co_name
        print(str(__class__) + ' ' + _funcName)

        tested_code.packageFunction()


