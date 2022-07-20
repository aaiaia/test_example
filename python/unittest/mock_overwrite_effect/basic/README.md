# Command
run command `python3 -m unittest mock_overwrite_effect.py`

```bash
$ python3 -m unittest mock_overwrite_effect.py
<class 'mock_overwrite_effect.Test_changeFunction0'> test_0001_call_packageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is not exist!!!

.<class 'mock_overwrite_effect.Test_changeFunction0'> test_0002_overwritePathLibToTrue
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'mock_overwrite_effect.Test_changeFunction0'> test_0003_overwritePathLibToFalse
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is not exist!!!

.<class 'mock_overwrite_effect.Test_changeFunction0'> test_0004_overwritePathLibToTrue
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'mock_overwrite_effect.Test_changeFunction0'> test_0005_justRunPackageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'mock_overwrite_effect.Test_changeFunction0'> test_0006_justRunPackageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'mock_overwrite_effect.Test_changeFunction1'> test_0001_justRunPackageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'mock_overwrite_effect.Test_changeFunction1'> test_0002_justRunPackageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.<class 'mock_overwrite_effect.Test_changeFunction1'> test_0003_justRunPackageFunction
checking path: fileIsNeverExist.log
checking Path() function: <class 'pathlib.Path'>
fileIsNeverExist.log is exist

.
----------------------------------------------------------------------
Ran 9 tests in 0.002s

OK
```
