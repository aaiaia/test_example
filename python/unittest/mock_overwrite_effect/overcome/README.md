# Command
run command `python3 -m unittest overcome_mock_overwrite.py`

```bash
$ python3 -m unittest overcome_mock_overwrite.py
<class 'overcome_mock_overwrite.Test_changeFunction0'> test_0000_PathLibMockingUsingPatch_notExist
checking path: fileIsNeverExist.log
checking Path() function: <MagicMock name='Path' id='139914683993776'>
fileIsNeverExist.log is not exist!!!

.<class 'overcome_mock_overwrite.Test_changeFunction0'> test_0001_PathLibMockingUsingPatch_exist
checking path: mockingFileLoc.log
checking Path() function: <MagicMock name='Path' id='139914684120320'>
mockingFileLoc.log is exist

.<class 'overcome_mock_overwrite.Test_changeFunction0'> test_0002_call_packageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is not exist!!!

.<class 'overcome_mock_overwrite.Test_changeFunction0'> test_0003_overwritePathLibToTrue
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'overcome_mock_overwrite.Test_changeFunction0'> test_0004_overwritePathLibToFalse
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is not exist!!!

.<class 'overcome_mock_overwrite.Test_changeFunction0'> test_0005_overwritePathLibToTrue
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'overcome_mock_overwrite.Test_changeFunction0'> test_0006_justRunPackageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'overcome_mock_overwrite.Test_changeFunction0'> test_0007_justRunPackageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'overcome_mock_overwrite.Test_changeFunction1'> test_0000_PathLibMockingUsingPatch_notExist
checking path: fileIsNeverExist.log
checking Path() function: <MagicMock name='Path' id='139914684152320'>
fileIsNeverExist.log is not exist!!!

.<class 'overcome_mock_overwrite.Test_changeFunction1'> test_0001_PathLibMockingUsingPatch_exist
checking path: mockingFileLoc.log
checking Path() function: <MagicMock name='Path' id='139914683680800'>
mockingFileLoc.log is exist

.<class 'overcome_mock_overwrite.Test_changeFunction1'> test_0002_justRunPackageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'overcome_mock_overwrite.Test_changeFunction1'> test_0003_justRunPackageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'overcome_mock_overwrite.Test_changeFunction1'> test_0004_justRunPackageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.
----------------------------------------------------------------------
Ran 13 tests in 0.004s

OK
```
